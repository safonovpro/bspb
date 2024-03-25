select
    df."дата" as "Дата",
    df."Customer_id",
    sum("CNT") over (partition by "Customer_id" order by "дата" rows 2 preceding) as "CNT_3"
from "agg_month.Transaction" df
order by df."Customer_id", df."дата" desc;
