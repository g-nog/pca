from sklearn.datasets import fetch_mldata
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression

if __name__ == '__main__':
    # You can add the parameter data_home to wherever to where you want to download your data
    mnist = fetch_mldata('MNIST original')
    print(mnist.data.shape)
    print(mnist.target.shape)
    # test_size: what proportion of original data is used for test set
    train_img, test_img, train_lbl, test_lbl = train_test_split(
        mnist.data, mnist.target, test_size=1 / 7.0, random_state=0)
    print(train_img.shape)
    print(train_lbl.shape)
    print(test_img.shape)
    print(test_lbl.shape)

    scaler = StandardScaler()

    # Fit on training set only.
    scaler.fit(train_img)

    # Apply transform to both the training set and the test set.
    train_img = scaler.transform(train_img)
    test_img = scaler.transform(test_img)

    pca = PCA(n_components=.95)
    pca.fit(train_img)

    print(pca.n_components_)

    train_img = pca.transform(train_img)
    test_img = pca.transform(test_img)

    # all parameters not specified are set to their defaults
    # default solver is incredibly slow thats why we change it
    # solver = 'lbfgs'
    logisticRegr = LogisticRegression(solver='lbfgs')
    logisticRegr.fit(train_img, train_lbl)

    # Returns a NumPy Array
    # Predict for One Observation (image)
    logisticRegr.predict(test_img[0].reshape(1, -1))

    # Predict for Multiple Observations (images) at Once
    logisticRegr.predict(test_img[0:10])

    score = logisticRegr.score(test_img, test_lbl)
    print(score)

    df = pd.DataFrame(data=[[1.00, 784, 48.94, .9158],
                            [.99, 541, 34.69, .9169],
                            [.95, 330, 13.89, .92],
                            [.90, 236, 10.56, .9168],
                            [.85, 184, 8.85, .9156]],
                      columns=['Variance Retained',
                               'Number of Components',
                               'Time (seconds)',
                               'Accuracy'])

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
