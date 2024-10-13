SELECT "c"."login", COUNT("o"."id") AS "in_delivery_orders"
FROM "Couriers" "c"
LEFT JOIN "Orders" "o" ON "c"."id" = "o"."courierId"
WHERE "o"."inDelivery" = true
GROUP BY "c"."login"
ORDER BY "in_delivery_orders" DESC;