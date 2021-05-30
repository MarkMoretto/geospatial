package multidim

import (
	"fmt"
)

type Matrix2DI [][]int32
type Matrix2DF [][]float32

var printString string


func (m *Matrix2DI) NCols() (cnt int){
	cnt = len((*m)[0])
	return
}

func (m *Matrix2DF) NCols() (cnt int){
	cnt = len((*m)[0])
	return
}



func (m *Matrix2DI) PrintIndexRows() {
	pPrintString := &printString
	*pPrintString = "Index\tValue\n"
	for _, row := range *m {
		for ic, col := range row {
			*pPrintString += fmt.Sprintf("%d", col)
			// If the coumn count is less than the total number
			// of columns, add a tab.
			if ic < m.NCols() - 1 {
				*pPrintString += "\t"
			}
		}
		*pPrintString += "\n"
	}
	fmt.Print(printString)
}


func (m *Matrix2DF) PrintIndexRows() {
	pPrintString := &printString
	*pPrintString = "Index\tValue\n"
	for _, row := range *m {
		for ic, col := range row {
			// If the coumn count is less than the total number
			// of columns, add a tab.
			if ic < m.NCols() - 1 {
				*pPrintString += "\t"
			}			
			*pPrintString += fmt.Sprintf("%.6f", col)
		}
		*pPrintString += "\n"
	}
	fmt.Print(printString)
}
