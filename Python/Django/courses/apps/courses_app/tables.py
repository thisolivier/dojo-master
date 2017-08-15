def course_table(data):
    string = '<thead><th>Course Name</th><th>Description</th><th>Date Added</th><th>Actions</th></thead><tbody>'
    for record in data:
        new_entry = '<td>{}</td>'.format(record.name)
        new_entry += '<td>{}</td>'.format(record.desc)
        new_entry += '<td>{}</td>'.format(str(record.created_at))
        new_entry += '<td><a href="/courses/{}/destroy/">remove</a></td>'.format(record.id)
        string += new_entry
    string += '</tbody>'
    return string