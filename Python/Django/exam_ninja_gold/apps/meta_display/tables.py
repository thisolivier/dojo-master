def name_gold(data, limit = -1):
    # Initialise
    proto_string = ""
    count = 0

    # Begin table construction
    proto_string += "<table><thead>"
    proto_string += "<th>email<th>"
    proto_string += "<th>gold<th>"
    proto_string += "</thead><tbody>"

    # Add records
    for record in data:
        if count == limit:
            break
        
        user_link = "<a href='meta/user/{}'>{}</a>".format(record['id'], record['email'])

        record_string = "<tr>"
        record_string += '<td>{}</td><td>{}</td>'.format(user_link, record['gold'])
        record_string += "</tr>"
        proto_string += record_string
        count += 1

    proto_string += "</tbody></table>"
    return proto_string
