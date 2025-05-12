def paginate_df(df, page, per_page=10):
    start = (page - 1) * per_page
    end = page * per_page
    paginated_df = df[start:end]
    total_pages = (len(df) + per_page - 1) // per_page
    return paginated_df, total_pages
