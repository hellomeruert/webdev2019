//
//  ViewController.swift
//  Calculator
//
//  Created by Meruert Amambayeva on 9/4/19.
//  Copyright © 2019 Meruert Amambayeva. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBOutlet weak var displayResultLabel: UILabel!
    var typing = false
    var firstOperand:Double = 0
    var secondOperand:Double = 0
    var operationSign:String = ""
    var dotIsPlaced = false
    
    var currentInput:Double {
        get{
            return Double(displayResultLabel.text!)!
        }
        set{
            //чтобы убрать 0 при вводе
            let value = "\(newValue)"
            let valueArray = value.components(separatedBy: ".")
            if valueArray[1] == "0"{
                displayResultLabel.text = "\(valueArray[0])"
            }else{
                displayResultLabel.text = "\(newValue)"
            }
            typing = false
        }
    }
    
    @IBAction func numberPressed(_ sender: UIButton) {
        let number = sender.currentTitle!
// чтобы больше 20 символов не вводилось
        if typing {
        if (displayResultLabel.text?.count)! < 20 {
        displayResultLabel.text = displayResultLabel.text! + number
            }
    }
    else{
    displayResultLabel.text! = number
    typing = true
       }
    }
        
    @IBAction func operand(_ sender: UIButton) {
        operationSign = sender.currentTitle!
        firstOperand = currentInput
        typing = false
        dotIsPlaced = false
}
    func twoOperandsAction(operation:(Double, Double) -> Double){
        currentInput = operation(firstOperand, secondOperand)
        typing = false
    }

    @IBAction func equalitySignPressed(_ sender: UIButton) {
        dotIsPlaced = false
        if typing {
            secondOperand = currentInput
        }
        switch operationSign{
        case "+":
            twoOperandsAction{$0 + $1}
        case "-":
             twoOperandsAction{$0 - $1}
        case "×":
             twoOperandsAction{$0 * $1}
        case "÷":
             twoOperandsAction{$0 / $1}
        default:break
        
        }
    }
    @IBAction func clearButtonPressed(_ sender: UIButton) {
        firstOperand = 0
        secondOperand = 0
        currentInput = 0
        displayResultLabel.text = "0"
        typing = false
        operationSign = ""
        dotIsPlaced = false
        
    }
    @IBAction func plusMinusButtonPressed(_ sender: UIButton) {
        currentInput = -currentInput
        
    }
    @IBAction func percentageButtonPressed(_ sender: UIButton) {
        if firstOperand == 0{
            currentInput = currentInput/100
        }else{
            secondOperand = firstOperand * currentInput / 100
        }
        typing = false
    }
    @IBAction func squareRootButtonPressed(_ sender: UIButton) {
        currentInput = sqrt(currentInput)
    }
    @IBAction func dotButtonPressed(_ sender: UIButton) {
        if typing && !dotIsPlaced{
            displayResultLabel.text = displayResultLabel.text! + "."
            dotIsPlaced = true
        }else{
            if !typing && !dotIsPlaced{
                displayResultLabel.text = "0."
                
            }
        }
    }
}
