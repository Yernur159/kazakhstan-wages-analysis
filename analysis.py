"""Анализ средней номинальной зарплаты в Казахстане, 2012–2025 (данные БНС, taldau.stat.gov.kz)."""
import pandas as pd, json
r=pd.read_csv('data/wages_by_region.csv'); s=pd.read_csv('data/wages_by_sector.csv'); ri=pd.read_csv('data/real_wage_index.csv')
kz=r[r.region=='Казахстан'].set_index('year').avg_wage_kzt
reg=r[r.region!='Казахстан']
last=reg[reg.year==2025].copy(); last['vs_kz_pct']=(last.avg_wage_kzt/kz[2025]*100-100).round(1)
last=last.sort_values('avg_wage_kzt',ascending=False)
gap=reg.groupby('year').avg_wage_kzt.agg(['max','min']); gap['ratio']=(gap['max']/gap['min']).round(2)
sec=s.pivot(index='sector',columns='year',values='avg_wage_kzt')
sec_g=((sec[2025]/sec[2015])-1).mul(100).round(0).sort_values(ascending=False)
nom_g=(kz/kz.shift(1)*100).round(1)
real=ri.set_index('year').real_wage_index_pct_prev_year
cpi=(nom_g/real*100).round(1)  # подразумеваемый дефлятор
print('Казахстан 2025:',kz[2025],'| рост с 2015 в', round(kz[2025]/kz[2015],2),'раза')
print(last[['region','avg_wage_kzt','vs_kz_pct']].to_string(index=False))
print('Разрыв макс/мин регион:\n',gap.loc[[2012,2018,2022,2025]])
print('Рост по отраслям 2015→2025, %:\n',sec_g)
print('Реальный индекс:',real.to_dict())
above=(last.vs_kz_pct>0).sum(); print('Регионов выше средней:',above,'из',len(last))
json.dump({'years':list(range(2012,2026)),
 'kz':[int(v) for v in kz],
 'regions':{k:[None if pd.isna(v) else int(v) for v in g.set_index('year').avg_wage_kzt.reindex(range(2012,2026))] for k,g in reg.groupby('region')},
 'sectors':{k:[int(v) for v in sec.loc[k]] for k in sec.index},
 'real':{int(k):v for k,v in real.items()},
 'nominal':{int(k):v for k,v in nom_g.dropna().items()},
},open('data/dashboard_data.json','w',encoding='utf-8'),ensure_ascii=False)
