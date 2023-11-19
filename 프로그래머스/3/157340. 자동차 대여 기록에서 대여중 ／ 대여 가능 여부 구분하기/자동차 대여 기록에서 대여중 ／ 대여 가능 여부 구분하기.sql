-- 코드를 입력하세요
SELECT DISTINCT CAR_ID, MAX(IF (date('2022-10-16') BETWEEN start_date AND end_date,'대여중', '대여 가능')) AS AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
order by 1 desc