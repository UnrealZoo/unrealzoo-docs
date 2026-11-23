# Import Custom Assets

> 📌 Usage guidance for importing custom asset PAK files into UnrealZoo.

# Import Custom Assets into UnrealZoo

> UnrealZoo supports loading custom Unreal Engine assets through standard Unreal Engine PAK files.

Users only need to package their assets into a .pak file and place it into the UnrealZoo  Paks directory. UnrealZoo will automatically mount and scan these assets during startup.

---

## Quick Start

1. Place your custom assets in your UE project, eg. YourProject/Content/MyAssets/ 
1. Create a PAK file from those assets
1. Place the PAK file in .../UnrealZoo_UE5_6_v3.0.1/Windows/UnrealZoo_UE5_6/Content/Paks/ 
1. Start UnrealZoo - assets are automatically mounted
---

## Prerequisites

- Unreal Engine 5.6 
- UnrealZoo v3.0.0 or newer
- Basic familiarity with Unreal Engine asset creation
---

# Step 1. Create a PAK File

UnrealZoo follows Unreal Engine's standard PAK loading mechanism.

Please refer to Epic Games' official tutorial:

Official Tutorial

https://dev.epicgames.com/community/learning/tutorials/7Bj8/unreal-engine-example-project-loading-pak-files-at-runtime

The general process is:

1. Create a normal Unreal Engine project.
1. Import your custom assets.
1. Cook the assets.
1. Package them into a .pak file.
---

## 1. Organize Assets

Place all assets that should be exported into a PAK under a dedicated folder.

Example:

```plain text
Content/
└── MyAssets/
    ├── Meshes/
    ├── Materials/
    ├── Textures/
    └── Characters/
```

---

## 2. Create a Primary Asset Label

In the Content Browser:

```plain text
Right Click
 └── Miscellaneous
      └── Data Asset
           └── PrimaryAssetLabel
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/2d4a49be-cf67-4fdf-bb41-e70abde1796f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=32197a2436c2b50405b0e082076e992049f5de1992abcce4689623bb1eed483c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/2ecd5fa5-b2e6-47e3-9eba-11d5813d1215/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=b8e0f4dbcdd1311e61fb898558e6d0ffa9c7d26a4467aea840ceecbb2bf50464&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Create a new asset:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/96b421e1-c4da-4ecf-b162-02216c27a053/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=5b02bc10db1165d2fb2a9c4606f7ec989d99fee7dcda89f0179e075ef1b22f1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Configure the asset:

| Setting | Value |
| --- | --- |
| Chunk ID | 111 |
| Apply Recursively | Enabled |
| Cook Rule | Always Cook |



> Note:  ChunkId shall be any unique positive integer greater than 0 and must be unique within UnrealZoo. The two PAK files must be assigned distinct ChunkIds. Id 0 is reserved and unavailable for use. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/dbd904c8-7663-4d22-bd37-a7a9b9617766/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=03d20c3a6321068f919397f5109c3d0cc790425837d613522e10445b1c760d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


Next, add all assets intended for packaging into the PAK file to the Explicit Asset and Explicit Blueprint fields of the Data Asset. Conventional UAsset resources such as levels and meshes go into Explicit Asset, while character blueprints and similar blueprint assets are added to Explicit Blueprint.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/cf55643e-0d76-4464-afe6-40624c6dc8b4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=cbd30043c8f575f9d34394fa31883710d515b43c4c5ce65942a6f78711610b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 3. Configure Packaging

Open:

```plain text
Edit
 └── Project Settings
      └── Packaging
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/88d9f4bf-bcdd-4b2e-a5e1-854cfa0e4efb/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=22141c2ae0645f9bcc8d7578b8f9da79ee1762d098104de1f5e4c58d3828d6b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Open the Packaging pannel in Project Sttings.

Enable:

- Use Pak File
- Generate Chunks
Disable:

- Use Io Store
If “Use Io Store” is Enabled, please disable it. 

---

## 4. Configure Asset Manager

Open:

```plain text
Edit
 └── Project Settings
      └── Asset Manager
```

Open the Asset Manager pannel in Project Sttings.

Disable:

- PrimaryAssetLabel - Is Editor Only
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/d29bed84-5c92-45f1-8e51-497b93cac92a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=d00affcbc8c6f782f1a3d9300b1df8c7bc9281c37048720a8ddaa044f3c1551d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 5. Package the Project

Package the project using the typical workflow:

```plain text
Platforms
 └── Windows
      └── Package Project
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/63aec94a-21bc-4009-a0ee-95133efe4320/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=18982066d34005aebc949de93e9ffaae41a75211b5a9f2c76206fed6edca79b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


Choose an output directory:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/fa16a4a1-dfdc-49d1-bafa-af98afe866f3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=3a3c86cec5aa4fd45e346b6169bd4675aaa0c08e42b0c6f83b0fd7c824e432b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


 Wait for packaging to complete:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/88974130-29c8-4fda-a767-67804da5cb74/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=ba559cd131fb4de715970aa9fe02929a4f080dfddccc344ab68938d11b12f402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


Unreal Editor will notify you when the packaging is completed:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/d4cb05d3-f9dc-43c4-b990-58795f1cb750/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=31b57253f685d6a11fed9d7061aed34d0887a51ef2470c3d1b12b3f7f9884001&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 6. Locate the Generated PAK

After packaging, the generated PAK file can be found under:

```plain text
OutputPath/
└── Windows/
    └── YourProject/
        └── Content/
            └── Paks/
```

Example output:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/35d9cb65-73ac-4e18-b34f-003362578973/af2cd4f1-87e4-48a2-baff-f4cc269920f8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBOL23Z%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T070633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICjg5Gn6IlNj3caUcDw3uTS4wXfdDUDZ6qcs4fW1F4y2AiEAyBq0Kq6S11edvbhUgvwG2HAHFGJgE5M0tKY%2BYOJwaMUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDHFieywtkPEPC856LircA7aL6Gly7mzECXhcVlb6F5GMTnRBfsmSTCJbJtVKCsj7LmMhO3afAMAa1ltIz7k1bZjx5kIXTNutG%2FpIEGjBS8qPiO8sD08PDBV4Tyxj6YGaEUQIFPpGnFNbr4bg53iS0HOmdSAuWR6vu0RmxAvBF5QOy93uDMdMi3GlNvQhfaNeJKorcBLkf%2Bmj9JxhbfTLz99JF5ughfLeM7NQBYSKQa%2BQC4bmzeQzqGSuakwmEoRUeNUBCiBg0D21ImbkmjoZHbW2butHo27PXykUlwfunWM%2B0ki4gwGRAZydYVa8%2F%2B9gkkAzJQKwfLh8SAC2yiIWzvr9uisp3b7Lz%2BXHjTSHcZugGzU2KPnFNRpTrYOCvflBXTvRP1oQOrOg3xwJEh1RjxZYSQm1pYWyAD7xYasiEEmbnt4gZZP9ZnUqRM9a1FUu6VOGgh9WdjIAEJMuaXrvIV0Qg8PTfSc1pP%2B9yBwDwT5dqKW8xwIgefmjAHOcU4uPXT5rQuUeNwwfZoYfdCOqLQ4yzZbgx46qRkiRC5peHYQMBN1jNvr8XiKsjh%2FOM5gvAJCsbsAzdyrHVxcwBSp4iI1b26gFr2W9ZR%2BtuTGv3lLseZoYs0Jm%2FNmYP%2FAL8pUxn53lsFK1ZlvUabTZMK2Tj9gGOqUBzDnGVlWWq7qmk0M2Hb1pVYlRIIcFLHyxmoJvxy77U6y0jBoH2XaAjU5l%2B4gGRVemKsle42%2BWHGVRdP6gKtKMqyD86DANrhBJisI2BL%2FOnLa6pf4CGBWT5iE2sBBVgYZlX2zuZSyd%2Brg8pOE6Cbe%2FEDtgmsXxIymzQEnmln1SRM52fMEC9ujTJjDecywiX6VuUATwtNXfGCbaa9cKOfRBWMhjZtxP&X-Amz-Signature=8cd279319e19e53f4f1c5fbbdfb3136754ae0ac473a8365d90820a8a741c662b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Step 2. Import into UnrealZoo

After creating your .pak file, importing it into UnrealZoo only requires copying the file into the correct directory.

---

## Copy the PAK File

Place the generated .pak file into UnrealZoo's PAK directory.

Example:

```plain text
UnrealZoo-UE5/
└── UnrealZoo_UE5_6_v3.0.1/
    └── Windows/
        └── UnrealZoo_UE5_6/
            └── Content/
                └── Paks/
                    └── pakchunk111-Windows.pak
```

Multiple PAK files can be placed in this directory simultaneously.

---

## Start UnrealZoo

Launch UnrealZoo normally.

During startup, UnrealZoo will:

1. Search the Content/Paks/ directory.
1. Automatically mount all discovered PAK files.
1. Scan assets contained in the mounted PAKs.
