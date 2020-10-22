def create_email(data):
    return f"""
Hello,

You got a inquiry from a {data.get("client_type")},

    Customer Name: {data.get("full_name")}
    
    Customer Type: {data.get("client_type").title()}
    
    Email: {data.get("email")}
    
    Phone Number: {data.get("phone_number")}
    
    Message: {data.get("message")}

Regards,
Iconicto Postmaster
    """
