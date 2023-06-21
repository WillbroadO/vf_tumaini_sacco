from frappe import _

def execute(filters=None):
    columns = [
        {
            "label": _("Member"),
            "fieldname": "member",
            "fieldtype": "Link",
            "options": "Member",
            "width": 120
        },
        {
            "label": _("Qualification Criteria"),
            "fieldname": "qualification_criteria",
            "fieldtype": "Data",
            "width": 120
        }
    ]

    # Perform your custom logic to fetch qualified members based on the criteria
    qualified_members = get_qualified_members()

    data = []
    for member in qualified_members:
        row = {
            "member": member.member,
            "qualification_criteria": member.qualification_criteria
        }
        data.append(row)

    return columns, data

