package math.jim_beam

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(List(x1, y1, x2, y2, x3, y3) <- Source.stdin.getLines.drop(1).map(_.split("\\s").map(_.toDouble).toList)) {
      def doesIntersect(): Boolean = {
        val (a1, b1, a2, b2) = (y2-y1, x1-x2, y3, -x3)
        val (c1, c2) = (x1 * a1 + y1 * b1, 0)
        val det = a1*b2 - a2*b1
        if(det == 0) {
          val dist = Math.abs(c1 - c2) / Math.sqrt(Math.pow(a1/b1, 2) + 1)
          if(dist > 0)
            false
          else
            !(Math.max(0, x3) < Math.min(x1, x2) || Math.min(0, x3) > Math.max(x1, x2))
        } else {
          val (x, y) = ((b2*c1 - b1*c2) / det, (a1*c2 - a2*c1) / det)
          Math.min(x3, 0) <= x && x <= Math.max(x3, 0) &&
          Math.min(x1, x2) <= x && x <= Math.max(x1, x2) &&
          Math.min(y1, y2) <= y && y <= Math.max(y1, y2) &&
          Math.min(y3, 0) <= y && y <= Math.max(y3, 0)
        }
      }
      println(if(doesIntersect) "NO" else "YES")
    }
  }
}