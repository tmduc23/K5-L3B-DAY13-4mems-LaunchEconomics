"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # E[N] = 1 + (1-p) + (1-p)^2 + ... + (1-p)^(k-1) = (1 - (1-p)^k) / p
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại hoàn toàn = cả k lần đều sai = (1-p)^k; k=None thì chạy đến khi đúng.
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy đã tốn. Mẫu số: chỉ phần thành công.
    # Rút gọn ra 1/p, nên hệ số không phụ thuộc k.
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ lần chạy thuộc tập yêu cầu đang xét (A3 truyền vào reqs đã lọc theo loai).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:
        # B1, B3: cắt các lần chạy vượt giới hạn; yêu cầu cần nhiều hơn giới hạn
        # coi như chuyển nhân viên, nên không còn phút xem lại / làm lại.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Token và tool: cộng trên MỌI lần chạy, kể cả lần status == 'loi'. Giá tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool

    # Giờ nhân viên: hai cột _simulated → mọi số dẫn xuất phải ghi nhãn simulated.
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        # Phần tiền của lần chạy thứ 2 và 3 — dùng để trả lời "chạy lại tốn bao nhiêu".
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        # Mẫu số CHỈ đếm việc thành công, trong khi tử số đã cộng mọi lần chạy.
        cps=tong / thanh_cong,
        # Con số dễ gây nhầm: hoá đơn token + tool chia đều cho số yêu cầu.
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# ---------- Nhiệm vụ D1 · Cỡ mẫu ----------
# TODO CP4 (người viết code phiên 2): cỡ mẫu so hai tỉ lệ và các giới hạn khi chia theo cụm.
ICC = 0.02


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu MỖI NHÓM để phát hiện chênh p1 → p2 (kiểm định hai phía, so hai tỉ lệ).
    n = (z_{1-α/2}·√(2·p̄(1−p̄)) + z_{1-β}·√(p1(1−p1) + p2(1−p2)))² ÷ (p2 − p1)², làm tròn lên."""
    from statistics import NormalDist
    za = NormalDist().inv_cdf(1 - alpha / 2)    # 1,95996
    zb = NormalDist().inv_cdf(power)            # 0,84162
    pb = (p1 + p2) / 2
    tu = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(tu / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=ICC):
    """DE = 1 + (m − 1)·ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def m_toi_thieu(n_can, so_cum, icc=ICC):
    """m nhỏ nhất để c·m / (1 + (m − 1)·ICC) ≥ n_can.
    Biến đổi: c·m ≥ n·(1 − ICC) + n·ICC·m → m ≥ n·(1 − ICC) / (c − n·ICC). Vô nghiệm nếu c ≤ n·ICC (vượt trần c/ICC)."""
    if so_cum <= n_can * icc:
        return None
    return math.ceil(n_can * (1 - icc) / (so_cum - n_can * icc))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · Theo loại yêu cầu')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"chay/yc":>8s} {"cps":>9s} {"so_voi_12k":>11s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, con)
        ti_le_tc = (con['ket_qua'] == 'thanh_cong').mean()
        chay_moi_yc = con['so_lan_chay'].mean()
        print(f'{loai:10s} {len(con):6d} {ti_le_tc:8.1%} {chay_moi_yc:8.2f} '
              f'{r["cps"]:9,.0f} {r["cps"] / BASELINE:10.2f}x')

    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử, tách theo loại.
    print('\nA3 · Tỉ lệ ok theo lần thử (attempt)')
    ok = runs.assign(ok=(runs['status'] == 'ok').astype(int)).merge(
        reqs[['request_id', 'loai']], on='request_id')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok',
                         aggfunc='mean').round(3).to_string())

    # ---------- Nhiệm vụ A4 · Chi phí cố định trong phạm vi pilot ----------
    CO_DINH_THANG = 40_000_000     # đồng / tháng
    YC_MOI_THANG = 45_000          # yêu cầu / tháng ở quy mô đầy đủ
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, pham_vi)
    tc_mau = r_pv['thanh_cong']                       # việc thành công trong mẫu 1.200
    print('\nA4 · Chi phí cố định (phạm vi noi_dia + hang_nang)')
    print(f'So yeu cau trong pham vi: {len(pham_vi)} · thanh cong: {tc_mau} · '
          f'cps chua co dinh: {r_pv["cps"]:,.0f} d')
    for ten, he_so in [('45.000 yc/thang', 1.0), ('mot nua khoi luong', 0.5)]:
        tc_thang = YC_MOI_THANG * he_so * tc_mau / len(reqs)
        co_dinh_moi_viec = CO_DINH_THANG / tc_thang
        cps_tong = r_pv['cps'] + co_dinh_moi_viec
        print(f'{ten:20s} tc/thang {tc_thang:9,.0f} · co dinh/viec {co_dinh_moi_viec:7,.0f} d '
              f'· cps {cps_tong:8,.0f} d = {cps_tong / BASELINE:.2f}x')


    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print(f'\nB1 · Độ nhạy (gốc {goc:,.0f} đ)')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:24s} {cps:9,.0f} {(cps / goc - 1) * 100:+7.1f}%')

    # ---------- Nhiệm vụ B2 · Đổi một cặp ----------
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ '
          f'({(cap / goc - 1) * 100:+.1f}%) — bằng tổng hai tác động riêng vì mô hình cộng tuyến tính')

    # ---------- Nhiệm vụ B3 · Giới hạn số lần chạy ----------
    print('\nB3 · Giới hạn số lần chạy (chi phí cả hệ thống = trợ lý + 12.000 đ × số yêu cầu không thành công)')
    print(f'{"gioi han":9s} {"tong tro ly":>12s} {"khong tc":>9s} {"ca he thong":>12s} {"cps":>9s}')
    for k in (1, 2, 3):
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        ko_tc = len(reqs) - r['thanh_cong']
        print(f'{k} lan     {r["tong"]:12,.0f} {ko_tc:9d} '
              f'{r["tong"] + ko_tc * BASELINE:12,.0f} {r["cps"]:9,.0f}')

    # ---------- Nhiệm vụ B4 · Nếu phải xem lại 100% ----------
    PHUT_XEM_LAI, PHUT_LAM_LAI = 5, 9      # giả định của đề cho kịch bản xem lại 100%
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()   # yêu cầu có ít nhất 1 lần ok
    so_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    tien_may = (runs_pv['tokens_in'] / 1000 * GIA_VAO
                + runs_pv['tokens_out'] / 1000 * GIA_RA
                + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = (pv['ket_qua'] == 'thanh_cong').sum()
    # Hai cách lấy số phút làm lại thực: trên toàn bộ ca lam_lai, và chỉ trong phạm vi.
    phut_toan_bo = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    phut_pham_vi = pv.loc[pv['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ({len(pv)} yêu cầu)')
    print(f'Yeu cau co it nhat 1 lan ok: {co_ok} · ca lam_lai: {so_lam_lai} · '
          f'token+tool: {tien_may:,.0f} d · viec thanh cong: {tc_pv}')
    for ten, phut in [(f'{PHUT_LAM_LAI} phut/ca (de cho)', PHUT_LAM_LAI),
                      (f'{phut_toan_bo:.1f} phut/ca (toan bo)', phut_toan_bo),
                      (f'{phut_pham_vi:.1f} phut/ca (pham vi)', phut_pham_vi)]:
        tong = co_ok * PHUT_XEM_LAI * LUONG_PHUT + so_lam_lai * phut * LUONG_PHUT + tien_may
        # Mức hoà vốn: mỗi lần xem lại dài tối đa bao nhiêu phút thì vẫn bằng 12.000 đ/việc
        hoa_von = (BASELINE * tc_pv - so_lam_lai * phut * LUONG_PHUT - tien_may) / (co_ok * LUONG_PHUT)
        print(f'Lam lai {ten:22s} tong {tong:12,.0f} d · cps {tong / tc_pv:8,.0f} d '
              f'= {tong / tc_pv / BASELINE:.2f}x · hoa von khi xem lai <= {hoa_von:.1f} phut')


    # ---------- Nhiệm vụ D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ----------
    SO_NHAN_VIEN = 40
    print('\nD1 · Cỡ mẫu mỗi nhóm')
    # a) Chia theo yêu cầu: mỗi yêu cầu độc lập, DE = 1.
    n_a = co_mau(0.70, 0.75)
    print(f'a) Chia theo yeu cau: co_mau(0.70, 0.75) = {n_a:,} yeu cau/nhom')

    # b) Chia theo nhân viên, mỗi người 75 yêu cầu: nhân cỡ mẫu với DE.
    de_b = he_so_thiet_ke(75)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhan vien, m = 75: DE = 1 + 74 x {ICC} = {de_b:.2f}; n = {n_a:,} x {de_b:.2f} = {n_b:,}/nhom '
          f'= {nv_b} nguoi/nhom, tong {2 * nv_b} > {SO_NHAN_VIEN} -> KHONG du nguoi')

    # c), d) Trần cỡ mẫu hiệu dụng: c·m/DE tiến tới c/ICC khi m → ∞, không bao giờ vượt.
    tran_c, tran_d = 20 / ICC, 6 / ICC
    print(f'c) 20 nhan vien/nhom: tran c/ICC = 20/{ICC} = {tran_c:,.0f} '
          f'{"<" if tran_c < n_a else ">="} {n_a:,} -> {"KHONG dat" if tran_c < n_a else "dat"} muc chenh 5 diem')
    print(f'd) 6 depot/nhom: tran 6/{ICC} = {tran_d:,.0f} -> loai (chi 6 cum, duoi 20)')

    # e) Nâng mức chênh lên 6 điểm, giữ 20 nhân viên mỗi nhóm: tìm m.
    n_e = co_mau(0.70, 0.76)
    m_e = m_toi_thieu(n_e, 20)
    print(f'e) Muc chenh 6 diem: co_mau(0.70, 0.76) = {n_e:,}/nhom; 20m/(1 + (m-1) x {ICC}) >= {n_e} '
          f'-> m >= {m_e} yeu cau/nguoi (DE {he_so_thiet_ke(m_e):.2f})')

    # Con số bất lợi: nếu tác động thật chỉ 5 điểm mà thiết kế cho 6 điểm (n hiệu dụng = 859).
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize
    power_5 = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70), nobs1=n_e, alpha=0.05)
    print(f'   Danh doi: neu tac dong that chi 5 diem, power voi n = {n_e} chi con {power_5:.2f}')

    # Tỉ lệ mở lại 7 ngày hiện tại — phải có TRƯỚC khi đặt ngưỡng an toàn trong luật dừng.
    pham_vi_d = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai = reqs['mo_lai_trong_7_ngay']
    mo_lai_pv = pham_vi_d['mo_lai_trong_7_ngay']
    print(f'\nTi le mo_lai_trong_7_ngay hien tai: toan bo {mo_lai.mean():.2%} ({mo_lai.sum()}/{len(reqs)}) · '
          f'noi_dia + hang_nang {mo_lai_pv.mean():.2%} ({mo_lai_pv.sum()}/{len(pham_vi_d)})')

    # ---------- Nhiệm vụ E1 · Ba chỉ số tính thử trên dữ liệu chạy thử ----------
    # Đợt chạy thử không có nhóm đối chứng: chỉ được viết "chỉ số trong đợt chạy thử là …".
    print('\nE1 · Ba chỉ số trong đợt chạy thử')
    # Chính (kết quả): đóng trong 24 giờ VÀ không mở lại trong 7 ngày, mẫu số là mọi yêu cầu.
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    # Dùng: tỉ lệ bỏ qua gợi ý = (sua + bo) / số yêu cầu ĐƯỢC XEM LẠI (không phải 1.200).
    # Ô trống của quyet_dinh_xem_lai đọc là '' nhờ keep_default_na=False.
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    # An toàn: tỉ lệ lỗi lọt đến khách = mở lại trong 7 ngày, mẫu số là mọi yêu cầu.
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    for ten, tu, mau in [('Chinh: dong 24h & khong mo lai 7 ngay', chinh.sum(), len(reqs)),
                         ('Dung: bo qua goi y (sua + bo)', bo_qua.sum(), len(xem)),
                         ('An toan: mo lai trong 7 ngay', an_toan.sum(), len(reqs))]:
        print(f'{ten:40s} {tu / mau:7.2%} ({tu}/{mau})')
    print('   Chi tiet quyet_dinh_xem_lai:', xem['quyet_dinh_xem_lai'].value_counts().to_dict())
