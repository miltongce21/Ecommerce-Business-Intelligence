# Project 02: Data-Driven Business Analytics of an Online Store: Customer Behavior, Revenue Trends, and Performance Analysis.
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("C:\\Users\\Lenovo\\Desktop\\Pycharm\\Online-Store-Orders.xlsx")
print(df)
# Total Number of Orders.
orders=df["OrderID"].count() # counts total No. of Orders.
print("Total No. of orders:",orders)
# Calculating Total Revenue.
Total_revenue=df["TotalPrice"].sum() # counts total revenue of the store.
print("Total revenue:",Total_revenue)
# Finding Number of unique orders.
print("Number of unique orders:",df["OrderID"].nunique())
# Finding Number of unique CustomerID.
print("Number of unique CustomerID:",df["CustomerID"].nunique())
# Counting Order per coupon code.
print("Orders per Coupon Code :")
print(df["CouponCode"].value_counts()) # FREESHIP is the highest and SAVE 10 is the lowest used Coupon code.
# Counting Order per ReferralSource.
print("Orders per ReferralSource :")
print(df["ReferralSource"].value_counts()) # Instagram is mostly used referral source.
# Counting Payment method used per Order.
print("Payment Method used :")
print(df["PaymentMethod"].value_counts()) # Mostly used payment method is Online and Gift card is less used.
# counting order status.
print("Order status count:")
print(df["OrderStatus"].value_counts()) # Highest No. orders were canceled.
# Counting types of product sale.
print("Product count:")
print(df["Product"].value_counts()) # Printer is the highest No. of Product sold where Phone is the lowest.
# Coupon brings higher-value orders and Lower value orders.
print("Coupon code analysis :")
Coupon_with_Revenue=df.groupby('CouponCode')["TotalPrice"].mean().sort_values(ascending=False)
print("Coupon brings higher and lower value orders :")
print(Coupon_with_Revenue) # FREESHIP bring higher value order and WINTER15 bring lower value order.
# Total revenue per coupon.
print("total revenue per coupon code :")
revenue_per_coupon=df.groupby('CouponCode')["TotalPrice"].sum().sort_values(ascending=False)
print(revenue_per_coupon) # FREESHIP bring higher revenue and WINTER15 bring lower revenue.
# Referral source brings higher or lower value orders.
avg_Referral_source=df.groupby('ReferralSource')["TotalPrice"].mean().sort_values(ascending=False)
print("Referral source brings higher and lower value orders :")
print(avg_Referral_source) # Facebook brings higher value where Refferal brings lower.
# total revenue per referral source.
print("total revenue per referral source")
total_revenue=df.groupby('ReferralSource')["TotalPrice"].sum().sort_values(ascending=False)
print(total_revenue) #Instagram provides higher and Referral provides lower revenue.
# No. of orders per customer.
print("No. of orders per customer :")
customer_orders=df.groupby('CustomerID')["OrderID"].nunique()
print(customer_orders.head(5)) # Most of the customers are unique.
# Amount each customer spend.
customer_spend=df.groupby('CustomerID')["TotalPrice"].sum().sort_values(ascending=False)
print("Amount each customer spend")
print(customer_spend.head(5)) # C38840 spend higher.
# Orders per month.
df['Date']=pd.to_datetime(df['Date'])
orders_per_month=df.groupby(df["Date"].dt.to_period('M')).size()
print("No. of orders per month :")
print(orders_per_month) # 2023-01 has the highest order frequency.
# Total revenue per month.
Revenue_per_month=df.groupby(df["Date"].dt.to_period('M'))["TotalPrice"].sum().sort_values(ascending=False)
print("Revenue per month")
print(Revenue_per_month) # 2024-06 has the highest revenue and 2023-04 has the lowest.
# Growth analysis (Time series analysis)
print("Growth analysis:")
Growth=Revenue_per_month.pct_change()*100
print("Growth analysis:")
print(Growth) # Growth of this store is decreasing in every month.
print("Growth of this store is decreasing in every month.")
# Customer Segmentation
Customer_expenditure=df.groupby('CustomerID')["TotalPrice"].sum().sort_values(ascending=False)
high_value_customers=Customer_expenditure[Customer_expenditure>2000]
low_value_customer=Customer_expenditure[Customer_expenditure<=2000]
print("Customer segmentation with Higher and lower value orders")
print("High value customers are:")
print(high_value_customers) # Best customers.
print("Low value customers are:")
print(low_value_customer) # worst customer.
# total revenue comes from the top customers. (>2000)
top_customer_revenue=high_value_customers.sum()
print("Total revenue from top customers:",top_customer_revenue)
# Percentage revenue comes from the top customers.
total_revenue=df["TotalPrice"].sum()
percentage_revenue=(top_customer_revenue/total_revenue)*100
print("Percentage(%)revenue of top customer:",percentage_revenue)
# products that provide top revenue
print("Products with top revenue:")
top_revenue_products=df.groupby('Product')["TotalPrice"].sum().sort_values(ascending=False)
print(top_revenue_products) # Chair is the top revenue generating product and Phone is the lowest revenue generating product.
#Order analysis
order_count=df["OrderStatus"].value_counts()
print(order_count)
# Total orders
total_order_count=df["OrderStatus"].value_counts().sum()
print("Total_orders:",total_order_count)
# percentage order status.
percentage_order_status=(order_count/total_order_count)*100
print("Percentage(%) orders status:")
print(percentage_order_status) # percentage of cancellation is high and % of delivered is low.
# RFM(Recency, Frequency, Monetary) analysis.
# Customer with lower Recency, Higher frequency and Monetary are the best customers
df["date"]=pd.to_datetime(df["Date"])
snapshot_date=df["Date"].max()+pd.Timedelta(days=1)
RFM=df.groupby('CustomerID').agg({
     'Date':lambda x:(snapshot_date-x.max()).days,
    'OrderID':'count',
    'TotalPrice':'sum',
})
RFM.columns=["Recency","Frequency","Monetary"]
print(RFM)
print("Customer with lower Recency, Higher frequency and Monetary are the best customers")
# Finding best customer
best_customers=RFM[(RFM["Recency"]<50) & (RFM["Frequency"]==1) & (RFM["Monetary"]>2000)]
print("Best customers:")
print(best_customers)
# Risky customers.
At_risk_customer=RFM[(RFM["Recency"]>50)&(RFM["Monetary"]>1000)]
print("At Risk customers:")
print(At_risk_customer)
# Low Value customers.
Low_value_customers=RFM[(RFM["Recency"]>100)&(RFM["Monetary"]<1000)]
print("Low value customers are:")
print(Low_value_customers)
# Coupon effectiveness analysis.
coupon_efficiency=df["CouponCode"].value_counts(normalize=True)*100
print("Coupon_efficiency analysis:",coupon_efficiency) # FREESHIP has higher efficiency and SAVE10 has lower efficiency.

# Data Visualization
## Revenue trend analysis corresponding to date.
revenue_per_date=df.groupby('Date')["TotalPrice"].sum().sort_index() # Revenue per date in chronological order.
plt.figure(figsize=(8,5))
plt.plot(revenue_per_date.index,revenue_per_date.values, color="maroon") # plot linear relationship between revenue and date.
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Revenue trend analysis")
plt.tight_layout()
plt.show()
# Insight : Highest revenue(9000$ approx.) was earned at 2023-08.
# Most of the days, the revenue was nearly consistent despite some highest revenue.
##  Total revenue per product
revenue_per_product=df.groupby('Product')["TotalPrice"].sum() # group products with their total price.
plt.figure(figsize=(8,5))
plt.bar(revenue_per_product.index,revenue_per_product.values, color="teal") # plot bar diagram to show the highest and lowest sale products.
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Total Revenue from each product")
plt.tight_layout()
plt.show()
# Total revenue from chair, printer and Laptop is higher, and revenue from phone is lower.
## showing the quantity of products sold.
product_quantity=df.groupby('Product')["Quantity"].sum() # group products with their total quantity.
plt.figure(figsize=(8,5))
plt.bar(product_quantity.index,product_quantity.values, color="tan") # plot bar diagram to the quantity sale of each product.
plt.xlabel("Product")
plt.ylabel("Product Quantity")
plt.title("Product Quantity trend analysis")
plt.tight_layout()
plt.show()
# Chair is the highest quantity sale product and phone is the lowest quantity sale product.
## Average revenue per product.
avg_revenue_per_product=df.groupby('Product')["TotalPrice"].mean() # mean value of each product.
plt.figure(figsize=(8,5))
plt.plot(avg_revenue_per_product.index,avg_revenue_per_product.values, color="red") # plot line graph to show avg revenue per product.
plt.xlabel("Product")
plt.ylabel("Average Revenue")
plt.title("Average Revenue from each product")
plt.tight_layout()
plt.show()
# customers spending tendency is more for laptop and less for phone.
## Revenue from each referral source.
Referral_Source_Revenue=df.groupby('ReferralSource')["TotalPrice"].sum() # Group referral source corresponding to total price.
plt.pie(Referral_Source_Revenue.values, labels=Referral_Source_Revenue.index , autopct='%1.1f%%',colors=['teal','orange','coral','aqua','purple'])
plt.title("(%) Revenue from each referral source")
plt.show()
# Higher revenue comes from instagram and Lower revenue comes from referral.
# Instagram is more profitable for marketing.
## payment method analysis
## Finding the highest and lowest using payment method.
plt.figure(figsize=(5,5))
Payment_method_preference=df.groupby('PaymentMethod').size().sort_values(ascending=False)
plt.bar(Payment_method_preference.index,Payment_method_preference.values, color="skyblue") #
plt.xlabel("Payment Method")
plt.ylabel("Order count")
plt.title("payment method analysis")
plt.tight_layout()
plt.show()
# Customers prefer Online payment method mose and prefer Gift card less during transaction.
## Order status analysis
Order_status=df["OrderStatus"].value_counts()
plt.pie(Order_status.values, labels=Order_status.index, autopct='%1.1f%%', colors=['red','coral','cyan','indigo','teal'])
plt.show()
# 20.8 % order was canceled, Returned 20.6 %, pending 19.8 %, shipped  19.6 %, delivered 19.2%.
## Correlation between Items in Cart and total revenue.
plt.scatter(df["ItemsInCart"],df["TotalPrice"], color="coral", marker="o")
plt.xlabel("Items in Cart")
plt.ylabel("Total Price")
plt.title("Correlation between Items in Cart and total revenue")
plt.tight_layout()
plt.show()
# Revenue increases with increasing the Items in cart. most of the customers purchase more items rather than single item.
# It shows Revenue of each purchase corresponding to the no. of items at each point.
# Column 8 has the highest cluster of sales as well as high-value sales. (More Transactions)
## Plotting histogram to visualize customer frequency.
customer_count=df["CustomerID"].value_counts()
plt.hist(customer_count, bins=3,color="navy",edgecolor="black")
plt.title("Frequency of customers")
plt.xlabel("No. of orders")
plt.ylabel("No. of unique customers")
plt.tight_layout()
plt.show()
# majority of the customers only placed single order. New customers are growing rapidly.
# customers comeback to place 2nd order are minimal in no.
# Business retention rate is low.
## Quantity product sold according to price.
plt.figure(figsize=(8,5))
plt.scatter(df["UnitPrice"],df["Quantity"], color="coral" )
plt.title("Frequency of customers")
plt.xlabel("UnitPrice")
plt.ylabel("Quantity of the products")
plt.tight_layout()
plt.show()
# products quantity sold looks like completely independent of product price.
# no trend to buy high-priced products in low quantity













