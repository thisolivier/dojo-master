def register():
    string = '''<div class="form-group">
                <label for="first_name">First Name</label>
                <input class="form-control" type="text" name="first_name">
            </div>
            <div class="form-group">
                <label for="last_name">Last Name</label>
                <input class="form-control" type="text" name="last_name">
            </div>
            <div class="form-group">
                <label for="email">Email Address</label>
                <input class="form-control" type="text" name="email">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input class="form-control" type="text" name="password">
            </div>
            <div class="form-group">
                <label for="email">Confirm Password</label>
                <input class="form-control" type="text" name="c_password">
            </div>'''
    return string

def login():
    string = '''<div class="form-group">
                <label for="email">Email Address</label>
                <input class="form-control" type="text" name="email">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input class="form-control" type="text" name="password">
            </div>'''
    return string