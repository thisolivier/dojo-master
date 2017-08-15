def table_design(query_data):
    table_string = '<table class="table"><thead><th>ID</th><th>Name</th><th>Email</th><th>Creation Date</th><th>Actions</th></thead><tbody>'
    actions_string = '<a href="/users/{}">Show</a> <a href="/users/{}/edit">Edit</a> <a href="/users/{}/delete">Delete</a>'
    for record in query_data:
        the_id = str(record.id)
        addString = '<tr><td>'
        addString += '{}</td>'.format(the_id)
        addString += '<td><a href="users/{}">'.format(the_id) + record.first_name + ' ' + str(record.last_name) + '</a></td>'
        addString += '<td>' + record.email + '</td>'
        addString += '<td>' + str(record.created_at) + '</td>'
        addString += '<td>' + actions_string.format(the_id, the_id, the_id) + '</td>'
        addString += '</tr>'
        table_string += addString
    table_string += '</table>'
    return table_string
