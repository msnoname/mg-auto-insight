import pandas as pd

def generate_sql_from_info(df, table_name="vehicle_sales_data"):
    """根据DataFrame的info()输出生成SQL"""
    
    type_mapping = {
        'object': 'TEXT',
        'int64': 'INTEGER',
        'float64': 'NUMERIC(10,2)',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'TIMESTAMP'
    }
    
    sql_lines = [f'CREATE TABLE "{table_name}" (']
    
    for col in df.columns:
        dtype = str(df[col].dtype)
        sql_type = type_mapping.get(dtype, 'TEXT')
        
        # 特殊处理某些字段
        if 'Engine (ltr)' in col and dtype == 'float64':
            sql_type = 'NUMERIC(10,2)'
        
        sql_lines.append(f'    "{col}" {sql_type},')
    
    sql_lines.append('    id BIGSERIAL PRIMARY KEY')
    sql_lines.append(');')
    
    return '\n'.join(sql_lines)

# 使用你的DataFrame
sql_statement = generate_sql_from_info(df_data)
print(sql_statement)