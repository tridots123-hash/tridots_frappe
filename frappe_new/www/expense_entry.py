import frappe
from frappe.utils import now,unique,random_string,validate_json_string,money_in_words,comma_and, today, add_days, format_duration, date_diff, cint, pretty_date, month_diff

def get_context(context):
    context.expenses = frappe.get_all(
        "Expense Entry",
        fields=["name","expense_date", "title", "amount", "status"],
        order_by="expense_date desc",
        limit_page_length=50,
    )
    # print("Now:", now())
    # print("Today:", today())
    # print("Add 5 days:", add_days(today(), 5))
    # # But yes, in casual terms you can call it days_diff, because it tells how many days difference between 2 dates.
    # print("Date diff:", date_diff("2025-06-02", today()))
    # print("Int Convert:", cint("10"))  # returns 10
    # diff = month_diff("2025-08-01", "2025-05-01")
    # print('month_diff',diff)  
    # pretty_date()
    # Just now, 2 minutes ago, 3 days ago, last week, a month ago
    # logs = [
    #     {"msg": "Invoice Created", "timestamp": now()},
    #     {"msg": "Reminder Sent", "timestamp": add_days(now(), -3)},
    #     {"msg": "Follow Up", "timestamp": add_days(now(), -30)},
    # ]
    # for log in logs:
    #     print(f"{log['msg']} — {pretty_date(log['timestamp'])}")
    # print(format_duration(90))          # Output: "1 minute 30 seconds"
    # print(format_duration(3661))        # Output: "1 hour 1 minute 1 second"
    # print(format_duration(0))           # Output: "0 seconds"
    # print(format_duration(3600 * 5))    # Output: "5 hours"  
    # print(comma_and(["apple", "banana", "cherry"]))
    # Output: "apple, banana and cherry"
    # print(money_in_words(4523.50, "INR"))
    # # Output: 'INR Four Thousand Five Hundred Twenty-Three and Fifty Paise Only'
    # print(money_in_words(1200.00, "USD"))
    # # Output: 'USD One Thousand Two Hundred Only'
    # validate_json_string() 
    # json_str = '{"name": "Macha", "age": 24}'
    # validate_json_string(json_str)  # ✅ No error
    # invalid_json = "{name: 'Macha', age: 24}"  # ❌ Not proper JSON (missing quotes, wrong format)
    # validate_json_string(invalid_json)
    # # ⚠️ Throws frappe.ValidationError: Invalid JSON string
    # print(random_string())         # e.g., 'X5bJp1mZ'
    # print(random_string(12))       # e.g., '8kJf29LsBxM3'
    # print(random_string(40)) # 'mcrLCrlvkUdkaOe8m5xMI8IwDB8lszwJsWtZFveQ'
    # random_string(6) # 'htrB4L'
    # random_string(6) #'HNRirG'
    # print(unique([1, 2, 3, 1, 1, 1])) # [1, 2, 3]
    # unique('abcda') # ['a', 'b', 'c', 'd']
    # unique(('Apple', 'Apple', 'Banana', 'Apple')) # ['Apple', 'Banana']