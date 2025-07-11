import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_reject_text(customer, ro_number, assembly_number,
                         serial_number, work_order_number,
                         part_number, reason, cmm_reference, corrective_action):

    prompt = f"""
You are creating a teardown/reject report for AeroRepair Corp.

Customer: {customer}
RO Number: {ro_number}
Assembly Number: {assembly_number}
Serial Number: {serial_number}
Work Order Number: {work_order_number}
Item Rejected: {part_number}
Reason for Rejection: {reason}
CMM Reference: {cmm_reference}
Corrective Action: {corrective_action or "Replace with new or serviceable item. Tagged red and quarantined."}

Format this as a professional teardown/reject report paragraph.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content'].strip()
