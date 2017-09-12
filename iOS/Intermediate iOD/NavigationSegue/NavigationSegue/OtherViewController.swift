//
//  OtherViewController.swift
//  NavigationSegue
//
//  Created by Olivier Butler on 12/09/2017.
//  Copyright © 2017 Olivier Butler. All rights reserved.
//

import UIKit

class OtherViewController : UIViewController{
    @IBOutlet weak var FailureLabel: UILabel!
    var Failure:String?
    
    @IBAction func DismissModalF(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        if let failure = Failure{
            FailureLabel.text = failure
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
