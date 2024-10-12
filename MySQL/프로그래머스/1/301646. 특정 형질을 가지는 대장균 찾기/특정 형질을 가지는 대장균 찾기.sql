-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 1 OR GENOTYPE & 4) AND !(GENOTYPE & 2)
# 2진수 계산 
# (1번 형질 : 1 -> 1, 3번 형질 : 4 -> 100)를 포함하며
# (2번 형질 : 2 -> 10)을 포함하지 않는 대장균
