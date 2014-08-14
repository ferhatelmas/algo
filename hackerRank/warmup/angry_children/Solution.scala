package warmup.angry_children

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val r = Source.stdin.getLines
    val (n, k) = (r.next.toInt, r.next.toInt)
    val ls = r.map(_.toInt).toArray.sorted
    println((0 to n-k).map(i => ls(i+k-1) - ls(i)).min)
  }
}
