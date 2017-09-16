//: Playground - noun: a place where people can play

import UIKit

struct Point {
    var X: Int
    var Y: Int
}

struct Line {
    var Start: Point
    var End: Point
    func length()->Double{
        let deltaX = abs(self.Start.X - self.End.X)
        let deltaY = abs(self.Start.Y - self.End.Y)
        var lengthCalc = Double(deltaX^2 + deltaY^2)
        print (lengthCalc)
        lengthCalc = sqrt(lengthCalc)
        return lengthCalc
    }
}

func lineTest(){
    let point1 = Point(X: 2, Y: 30)
    let point2 = Point(X: 12, Y: 18)
    let myLine = Line(Start: point1, End: point2)
    print (myLine.length())
}

struct Triangle {
    var Points: [Point]
    func area()->Double{
        if Points.count == 3 {
            var max:[Double] = [-.infinity, -.infinity]
            var min:[Double] = [.infinity, .infinity]
            
            func testExtreme(position: Point){
                let x = Double(position.X)
                let y = Double(position.Y)
                
                if x > max[0]{
                    max[0] = x
                } else if x < min[0]{
                    min[0] = x
                }
                
                if y > max[1]{
                    max[1] = y
                } else if y < min[1]{
                    min[1] = y
                }
            }
            
            func calcRightAngleAreaFromPoints(start:Point, end:Point)-> Double{
                let deltaX = abs(start.X - end.X)
                let deltaY = abs(start.Y - end.Y)
                print("Calculating area of triangle with right angle sides \(deltaX), and \(deltaY)")
                let area = Double(deltaY * deltaX)/2
                print (area)
                return (area)
            }
            
            
            for point in self.Points{
                testExtreme(position: point)
            }
            
            let deltaX = abs(max[0] - min[0])
            let deltaY = abs(max[1] - min[1])
            var boundingArea = deltaY * deltaX
            print ("The bounding area is \(boundingArea)")
            
            var area1 = calcRightAngleAreaFromPoints(start: Points[0], end: Points[1])
            var area2 = calcRightAngleAreaFromPoints(start: Points[1], end: Points[2])
            var area3 = calcRightAngleAreaFromPoints(start: Points[0], end: Points[2])
            var totalTriangles = area1 + area2 + area3
            print ("The triangle total is \(totalTriangles)")
            
            return (boundingArea - totalTriangles)
        } else {
            print ("More than 3 points in triangle")
            return -1
        }
    }
}

func triangleTest() -> Double{
    let pointArray = [Point(X: 8, Y: 39), Point(X: 52, Y: 30), Point(X: 2, Y: 17)]
    let myTriangle = Triangle(Points: pointArray)
    return myTriangle.area()
}

print ("My triangle has an area of \(triangleTest())")