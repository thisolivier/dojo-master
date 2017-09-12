//
//  ViewController.swift
//  NavigationSegue
//
//  Created by Olivier Butler on 12/09/2017.
//  Copyright © 2017 Olivier Butler. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var darkZoneTextInput: UITextField!
    
    @IBAction func DismissModalF(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any!) {
        if let _ = segue.identifier {
            let destination = segue.destination as! OtherViewController
            destination.Failure = darkZoneTextInput.text
        }
    }
}
