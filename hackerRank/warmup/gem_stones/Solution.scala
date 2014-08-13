package warmup.gem_stones

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    val lines = Source.stdin.getLines
    val n = lines.next.toInt
    val ls = Array.fill[Int](26)(0)
    for(s <- lines.map(_.toSet)) {
      s.foreach(c => ls(c - 'a') += 1)
    }
    println(ls.filter(i => i == n).length)
  }
}
