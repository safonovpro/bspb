select * from "Customer" where "ID" in (
    select distinct "Customer_id" from "CustomerProduct"
    where
        "Тип_Продукта" = 'Потреб' and
        "Дата начала действия" <= current_date and
        "Дата окончания действия" >= current_date and
        current_is_active
) and "Возраст" < 65
order by "ID";
