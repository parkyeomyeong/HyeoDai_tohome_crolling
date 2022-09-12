import re

prod_id = "javascript: GA_Event('PC_카테고리', '상품', '[만전식품] 일회조 오사리(조미) 전장10매(40g)x3봉');  GA_DpDawnEcomm('S02006002088', '[만전식품] 일회조 오사리(조미) 전장10매(40g)x3봉', '만전식품(주)', '배송/건식품/김_미역/김', '8802241132067','112182_만전식품(주)','A10139_만전식품(주)', '일반상품','건식(1501)', '카테고리_100615_생선과 해산물, 건어물', '100615_생선과 해산물, 건어물', ''); fnProductDetailMove('S02006002088','104004','100735');"
# params = re.compile(r"^'.+'$")
print(prod_id.find("fnProductDetailMove"))
params = re.findall(r"'.*'", prod_id[prod_id.find("fnProductDetailMove"):])
p = [string.strip("'") for string in params[0].split(',')]
