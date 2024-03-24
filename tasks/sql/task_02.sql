select distinct on (c."ID")
    c."ID" as customer_id,
    t."дата"::date as date,
    crd."тип_карты" as card_type
from "Transaction" t
left join "Card" crd on crd."ID" = t."ID_карта"
left join "Customer" c on crd."Customer_id" = c."ID"
order by c."ID", t."дата" desc;
