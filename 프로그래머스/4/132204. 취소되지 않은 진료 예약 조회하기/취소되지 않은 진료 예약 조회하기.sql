select a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
from DOCTOR d
join APPOINTMENT a
on d.DR_ID = a.MDDR_ID
join PATIENT p
on p.PT_NO = a.PT_NO
where a.APNT_CNCL_YN = 'N' and a.APNT_YMD like '2022-04-13 %'
order by a.APNT_YMD