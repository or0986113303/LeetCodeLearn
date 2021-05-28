package hourglassSum

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

func HourglassSum(arr [][]int32) int32 {
	// Write your code here

	weight := len(arr[0])
	height := len(arr)
	var maxsum int32

	for y := 1; y < height-1; y++ {
		for x := 1; x < weight-1; x++ {
			sumtmp := arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1] +
				arr[y][x] +
				arr[y-1][x-1] + arr[y-1][x] + arr[y-1][x+1]

			if maxsum < sumtmp {
				maxsum = sumtmp
			}
			if sumtmp > maxsum {
				maxsum = sumtmp
			}
		}
	}
	return maxsum
}
