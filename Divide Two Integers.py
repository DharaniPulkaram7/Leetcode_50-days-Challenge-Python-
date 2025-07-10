class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of the quotient
        negative = (dividend < 0) != (divisor < 0)
        
        # Convert to positive numbers (use abs carefully to avoid overflow)
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        # Subtract divisor multiples from dividend
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1
            # Increase the divisor by doubling it (bit shifting) to speed up
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract and add multiple to quotient
            dividend_abs -= temp
            quotient += multiple
        
        # Apply sign
        if negative:
            quotient = -quotient
        
        # Clamp to 32-bit signed integer limits
        return max(min(quotient, INT_MAX), INT_MIN)
