package warmup.sherlock_and_gcd

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    def cgcd(a: Int, b: Int): Int = if(b == 0) a else cgcd(b, a%b)
    def gcd(ls: List[Int]): Int = ls match {
      case x :: List() => x
      case x :: lls => cgcd(x, gcd(lls))
    }
    val lines = Source.stdin.getLines
    (0 until lines.next.toInt).foreach(_ => {
      if(gcd(lines.drop(1).next.split("\\s").map(_.toInt).toList) == 1)
        println("YES")
      else
        println("NO")
    })
  }
}
