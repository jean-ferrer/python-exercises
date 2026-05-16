# 2026-05-16

import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    
    borrowing_records = borrowing_records.drop(columns=['record_id', 'borrower_name', 'borrow_date'])
    borrowing_records = borrowing_records[borrowing_records['return_date'].isnull()]
    borrowed = borrowing_records.value_counts('book_id').reset_index()

    merge_borrowed = pd.merge(library_books, borrowed, how='left')
    merge_borrowed = merge_borrowed[merge_borrowed['total_copies'] == merge_borrowed['count']]

    merge_borrowed = merge_borrowed.drop(columns=['count'])
    merge_borrowed = merge_borrowed.rename(columns={'total_copies': 'current_borrowers'})
    merge_borrowed = merge_borrowed.sort_values(by=['current_borrowers', 'title'], ascending=[False, True])

    return merge_borrowed