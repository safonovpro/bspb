create or replace view "agg_month.Transaction" as
    select
        date_trunc('month', t."дата")::date as "дата",
        c."Customer_id",
        count(t.*) as "CNT"
    from "Transaction" t
    left join "Card" c on t."ID_карта" = c."ID"
    group by date_trunc('month', t."дата")::date, c."Customer_id"
    order by c."Customer_id", date_trunc('month', t."дата")::date desc;