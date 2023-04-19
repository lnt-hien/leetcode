def generate(self, numRows: int) -> List[List[int]]:
    result = []
    
    for r in range(numRows):
        row = []
        for ele in range(r+1):
            if ele == 0 or ele == r:
                row.append(1)
            else:
                row.append(result[r-1][ele-1] + result[r-1][ele])
        
        result.append(row)
        
    return result