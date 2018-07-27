@NEED_LOGIN

Feature: AddGoodPage

    Background: log in and go to specified page
        Given click menu "商品管理" and "商品发布" and bread_crumb as "商品发布"

    Scenario: 发布有效商品
        When I specify below valid good info to add good
            | name   | element_type | element_xpath                    | value           |
            | 商品简称   | input        | //input[@id='name']              | 大胖石锅鱼情侣       |
            | 商品名称   | input        | //input[@id='fullName']          | 大胖石锅鱼情侣套餐 够辣    |
            | 副标题    | input        | //input[@id='briefIntroduction'] | 大胖石锅鱼情侣套餐 够辣 管饱 |
            | 商品分类   | select       | //td[@id='proCate']/select       | 餐饮美食            |
            | 市场价    | input        | //input[@id='marketPrice']       | 200             |
            | 团购价    | input        | //input[@id='price']             | 99              |
            | 库存量    | input        | //input[@id='store']             | 1000            |
            | 限购数量   | input        | //input[@id='max']               | 100             |
            | 团购开始日期 | date_picker  | //input[@id='startTime']         | 2018-05-10 17:54:03         |
            | 团购结束日期 | date_picker  | //input[@id='endTime']           | 2018-05-20 17:54:03  |
            | 验证码有效期 | date_picker  | //input[@id='expireEndTime']     | 2018-05-20 17:54:03  |
            | 购买须知   | input        | //textarea[@id='buyKnow']           | 购买须知 大胖石锅鱼情侣套餐  |
            | 商品详情   | input        | //tbody//iframe                  | 商品详情  大胖石锅鱼情侣套餐 |
        And upload good photoes, file name as "logo.jpg"
        And check submit for approval
        And click to save good
        Then should get good in good list
        # 调用其他服务
        Given I do preapprove for sale in bank
        # 回来
        Given click menu "商品管理" and "商品查询" and bread_crumb as "商品查询"