"""Example implementing a list utility funciton."""

#Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
# RV = True iff needle is in haystack and False otherwise
def contains(needle: str, haystack: list[str]) -> bool:
    """Loops through a list to find if one value exists within it."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            # We found it! No more work to do!
            return True
        i += 1
    # We tried searching each item and came up short!
    return False
    


    
   
        
        
    