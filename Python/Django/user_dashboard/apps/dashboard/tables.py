from ..login_reg.models import User

def all_table(admin):
    user_query = User.objects.all().order_by('created_at');
    table_string = """
        <table class="table">
            <thead>
                <th>ID</th>
                <th>Full Name</th>
                <th>email</th>
                <th>created at</th>
                <th>user level</th>"""
    if admin:
        table_string +=  "<th>actions</th>"
    
    table_string += "</thead><tbody>"

    for user in user_query:
        table_string += "<tr>"
        table_string += "<td>" + str(user.id) + "</td>"
        table_string += '<td><a href="users/show/' + str(user.id) + '">' + user.first_name + " " + user.last_name + "</a></td>"
        table_string += "<td>" + user.email + "</td>"
        table_string += "<td>" + str(user.created_at) + "</td>"
        table_string += "<td>" + str(user.admin) + "</td>"
        if admin:
            table_string += '<td>'
            table_string += '<a href="/users/edit/' + str(user.id) + '">' + 'edit </a>' 
            table_string += '<a href="/users/remove/' + str(user.id) + '">' + 'remove' + "</a>"
            table_string += "</td>"
        table_string += "</tr>"
    
    table_string += """        
        </tbody>
    </table>"""

    return table_string

# def admin_query():
#     user_query = User.objects.all().order_by('created_at');
#     cols = [
#         ('ID', {'fields': 'id'}),
#         ('Full Name', {
#             'fields': [first_name, last_name],
#             'link_prefix' : 'users/show/'} ),
#         ('Email', {'fields': 'id'}),
#         ('Created at', {'fields': 'created_at'}),
#         ('User Level', {'fields': 'admin'}),
#         ('Actions', {'fields': 'actions'})
#     ]