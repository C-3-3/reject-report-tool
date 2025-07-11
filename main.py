from gpt_writer import generate_reject_text
from report_builder import generate_docx
from cmm_db import init_db, get_cmm_reference, add_cmm_entry

def main():
    print("=== Reject Report Generator ===\n")

    # Initialize the CMM database if not already created
    init_db()

    # Collect inputs
    part_number = input("Part Number: ")
    damage_type = input("Damage Type: ")

    # Try to find a CMM ref from the DB
    cmm = get_cmm_reference(part_number, damage_type)
    if not cmm:
        print("No CMM reference found. Add one now.")
        add_cmm_entry(part_number, damage_type)
        cmm = get_cmm_reference(part_number, damage_type)

    # Gather remaining inputs
    customer = input("Customer: ")
    ro_number = input("RO Number: ")
    assembly_number = input("Assembly Number: ")
    serial_number = input("Serial Number: ")
    work_order_number = input("Work Order Number: ")
    reason = input("Reason for Rejection: ")
    corrective_action = input("Corrective Action (optional): ")

    # Generate text via GPT
    report_text = generate_reject_text(customer, ro_number, assembly_number,
                                       serial_number, work_order_number,
                                       part_number, reason, cmm, corrective_action)

    # Create a .docx
    generate_docx(report_text, work_order_number)

    print("\n✅ Report generated successfully.")

if __name__ == "__main__":
    main()
