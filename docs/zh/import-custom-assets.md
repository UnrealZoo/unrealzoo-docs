# 导入自定义资产

> 📌 将自定义资产 PAK 文件导入 UnrealZoo 的使用指南。

UnrealZoo 支持通过标准 Unreal Engine PAK 文件加载自定义 Unreal Engine 资产。只需将资产打包为 .pak 文件并放入 UnrealZoo 的 Paks 目录，UnrealZoo 将在启动时自动挂载并扫描这些资产。

---

## 快速开始

1. 将自定义资产放入 UE 项目，例如 `YourProject/Content/MyAssets/`
2. 基于这些资产创建 PAK 文件
3. 将 PAK 文件放入 `.../UnrealZoo_UE5_6_v3.0.1/Windows/UnrealZoo_UE5_6/Content/Paks/`
4. 启动 UnrealZoo，资产将自动挂载

---

## 前置条件

- Unreal Engine 5.6
- UnrealZoo v3.0.0 或更新版本
- 基本熟悉 Unreal Engine 资产创建

---

## 步骤 1. 创建 PAK 文件

UnrealZoo 遵循 Unreal Engine 的标准 PAK 加载机制。请参考 Epic Games 官方教程：

官方教程

https://dev.epicgames.com/community/learning/tutorials/7Bj8/unreal-engine-example-project-loading-pak-files-at-runtime

大致流程如下：

1. 创建一个普通的 Unreal Engine 项目
2. 导入自定义资产
3. 烹饪（Cook）资产
4. 打包为 .pak 文件

---

### 1. 组织资产

将所有需要导出到 PAK 的资产放入一个专用文件夹中。示例：

```plain text
Content/
└── MyAssets/
    ├── Meshes/
    ├── Materials/
    ├── Textures/
    └── Characters/
```

---

### 2. 创建 Primary Asset Label

在 Content Browser 中：

```plain text
Right Click
 └── Miscellaneous
      └── Data Asset
           └── PrimaryAssetLabel
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/2d4a49be-cf67-4fdf-bb41-e70abde1796f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=32197a2436c2b50405b0e082076e992049f5de1992abcce4689623bb1eed483c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/2ecd5fa5-b2e6-47e3-9eba-11d5813d1215/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=b8e0f4dbcdd1311e61fb898558e6d0ffa9c7d26a4467aea840ceecbb2bf50464&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

创建一个新资产：

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/96b421e1-c4da-4ecf-b162-02216c27a053/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=5b02bc10db1165d2fb2a9c4606f7ec989d99fee7dcda89f0179e075ef1b22f1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

配置该资产：

| 设置 | 值 |
| --- | --- |
| Chunk ID | 111 |
| Apply Recursively | Enabled |
| Cook Rule | Always Cook |

> 注意：ChunkId 应为任意大于 0 的唯一正整数，且在 UnrealZoo 内必须唯一。两个 PAK 文件必须分配不同的 ChunkId。Id 0 为保留值，不可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/dbd904c8-7663-4d22-bd37-a7a9b9617766/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=03d20c3a6321068f919397f5109c3d0cc790425837d613522e10445b1c760d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来，将所有需要打包进 PAK 文件的资产添加到该 Data Asset 的 Explicit Asset 和 Explicit Blueprint 字段中。关卡、网格体等常规 UAsset 资源放入 Explicit Asset，角色蓝图及类似蓝图资产则添加到 Explicit Blueprint。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/cf55643e-0d76-4464-afe6-40624c6dc8b4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=cbd30043c8f575f9d34394fa31883710d515b43c4c5ce65942a6f78711610b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 3. 配置打包

打开：

```plain text
Edit
 └── Project Settings
      └── Packaging
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/88d9f4bf-bcdd-4b2e-a5e1-854cfa0e4efb/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=22141c2ae0645f9bcc8d7578b8f9da79ee1762d098104de1f5e4c58d3828d6b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 Project Settings 中打开 Packaging 面板。

启用：

- Use Pak File
- Generate Chunks

禁用：

- Use Io Store

若 “Use Io Store” 处于启用状态，请将其禁用。

---

### 4. 配置 Asset Manager

打开：

```plain text
Edit
 └── Project Settings
      └── Asset Manager
```

在 Project Settings 中打开 Asset Manager 面板。

禁用：

- PrimaryAssetLabel - Is Editor Only

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/d29bed84-5c92-45f1-8e51-497b93cac92a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln