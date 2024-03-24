select c.*, kgd."Отделение" from "Customer" c
left join "Customer_KGD" kgd on c."ID" = kgd."Customer_id"
    where c."ID" in (
        select distinct "Customer_id" from "CustomerProduct"
        where
            "Тип_Продукта" = 'Потреб' and
            "Дата начала действия" <= current_date and
            "Дата окончания действия" >= current_date and
            current_is_active
    ) and
    c."Возраст" < 65 and
    c."Программа_лояльности" = 'Travel' and
    kgd."Отделение" like '%Санкт-Петербург'
order by "ID";
