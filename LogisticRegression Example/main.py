import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
import loguru



if __name__ == '__main__':
    ### 原始數據清理
    df_original = pd.read_csv('Rawdata.csv')

    # 使用布林索引選擇 name 列中不包含 "麥片" 的行
    df_filtered = df_original[~df_original['name'].str.contains('麥片')]

    # 將totals中的字串型別的數字轉成整數型態數字
    df_filtered['totals'] = df_filtered['totals'].str.replace(',', '').astype(int)
    df_filtered = df_filtered.sort_values(by='totals', ascending=False)

    df_filtered.to_csv('FilteredData.csv', index=False)



    ### 使用監督式學習中的 LogisticRegression來做為品牌辨識工程的主要Model
    # 準備數據 (需要人工標記後的FilteredData，並儲存成FilteredData_tag)
    df_tag_filtered = pd.read_csv('FilteredData_tag.csv')
    X = df_tag_filtered['name']
    y =  df_tag_filtered['Brand']


    vectorizer = TfidfVectorizer()
    X_tfidf = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.3, random_state=114514)

    model = LogisticRegression(class_weight='balanced', C=114514)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    loguru.logger.debug(f'Model Accuracy: {accuracy}')
    loguru.logger.debug(f'Model Precision: {precision}')


    # 將模型應用到去掉"麥片"這個品項的資料集
    df_filtered['Brand'] = model.predict(X_tfidf)


    # 儲存處理後的資料到新的CSV檔案
    df_filtered.to_csv('Processed_Data.csv', index=False)
