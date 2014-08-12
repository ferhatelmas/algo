package warmup.is_fibo

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    lazy val fibs: Stream[BigInt] = 0 #:: 1 #:: fibs.zip(fibs.tail).map { n => n._1 + n._2 }
    for(i <- Source.stdin.getLines.drop(1).map(BigInt(_))) {
      println(if(fibs.dropWhile(j => j < i).head == i) "IsFibo" else "IsNotFibo")
    }
  }
}
