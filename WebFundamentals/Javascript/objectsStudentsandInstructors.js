var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
    ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
    ]
}

function outputNames(arr) {
    for (var i = 0; i < obj.length; i++){
        console.log(arr[i].first_name + " " + arr[i].last_name);
    }
}

function nitroNames(obj) {
    function printer(key){
        console.log(key);
        var arr = obj[key];
        for (var i = 0; i < arr.length; i++){
            var first = arr[i].first_name,
                last = arr[i].last_name;
            console.log (i + " - " + first + " " + last + " - " + (first.length + last.length));
        }
    }
    printer("Students");
    printer("Instructors");
}