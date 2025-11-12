Problem Statement

Imagine you’re building a payment system for your application.
Your code is designed to work with a specific payment interface, say Razorpay.
But now your manager says:
“We need to add PayPal support too!”
The issue is:
Your existing code expects all payment gateways to have a standard interface (like make_payment(amount)).
But PayPal’s SDK has different method names and parameters, like send_money(value, currency).
So — how do we make PayPal work without rewriting our entire payment processing code?

Adaptive Approach (Using Adapter Pattern)
💡 Idea:

Create a common interface (Target) expected by the client (your app).
Then, create adapters that wrap each incompatible class and translate their interface to match the expected one.