with df as(
    select
        df."дата" as "Дата",
        df."Customer_id",
        sum("CNT") over (partition by "Customer_id" order by "дата") as "CNT_3"
    from "agg_month.Transaction" df
    order by df."Customer_id", df."дата" desc
) select * from df where "Дата" >= '2024-01-01';
