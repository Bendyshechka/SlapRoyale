local OrionLib = loadstring(game:HttpGet(('https://raw.githubusercontent.com/Articles-Hub/ROBLOXScript/refs/heads/main/Library/Orion/Source.lua')))()
loadstring(game:HttpGet("https://raw.githubusercontent.com/Giangplay/Script/main/Fly_V3.lua"))()
local Window = OrionLib:MakeWindow({Name = "Сигма Слеп Халяль", HidePremium = false, SaveConfig = false})

local function Press()
    local VirtualInputManager = game:GetService("VirtualInputManager")

-- Нажимаем клавишу "E"
VirtualInputManager:SendKeyEvent(true, Enum.KeyCode.F, false, game)
-- Отпускаем клавишу "E" (можно задержать, если нужно)
task.wait(0.1)  -- Задержка перед отпусканием (опционально)
VirtualInputManager:SendKeyEvent(false, Enum.KeyCode.F, false, game)
end

local Tab2 = Window:MakeTab({
	Name = "Имба",
	Icon = "rbxassetid://4483345998",
	PremiumOnly = false
})

Tab2:AddButton({
	Name = "Открыть лабараторию",
	Callback = function()
if game.Workspace.Map.CodeBrick.SurfaceGui:FindFirstChild("IMGTemplate") then
game.Workspace.Map.CodeBrick.SurfaceGui.IMGTemplate.Name = "1st"
game.Workspace.Map.CodeBrick.SurfaceGui.IMGTemplate.Name = "2nd"
game.Workspace.Map.CodeBrick.SurfaceGui.IMGTemplate.Name = "3rd"
game.Workspace.Map.CodeBrick.SurfaceGui.IMGTemplate.Name = "4th"
end
for i,v in pairs(game.Workspace.Map.CodeBrick.SurfaceGui:GetChildren()) do
                    if v.Name == "1st" then
                        if v.Image == "http://www.roblox.com/asset/?id=9648769161" then
                    first = "4"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648765536" then
                    first = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648762863" then
                    first = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648759883" then
                    first = "9"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648755440" then
                    first = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648752438" then
                    first = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648749145" then
                    first = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648745618" then
                    first = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648742013" then
                    first = "7"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648738553" then
                    first = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648734698" then
                    first = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648730082" then
                    first = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648723237" then
                    first = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648718450" then
                    first = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648715920" then
                    first = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648712563" then
                    first = "2"
                end
                    end
                end
for i,v in pairs(game.Workspace.Map.CodeBrick.SurfaceGui:GetChildren()) do
                    if v.Name == "2nd" then
                        if v.Image == "http://www.roblox.com/asset/?id=9648769161" then
                    second = "4"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648765536" then
                    second = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648762863" then
                    second = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648759883" then
                    second = "9"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648755440" then
                    second = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648752438" then
                    second = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648749145" then
                    second = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648745618" then
                    second = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648742013" then
                    second = "7"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648738553" then
                    second = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648734698" then
                    second = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648730082" then
                    second = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648723237" then
                    second = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648718450" then
                    second = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648715920" then
                    second = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648712563" then
                    second = "2"
                end
                    end
                end
for i,v in pairs(game.Workspace.Map.CodeBrick.SurfaceGui:GetChildren()) do
                    if v.Name == "3rd" then
                        if v.Image == "http://www.roblox.com/asset/?id=9648769161" then
                    third = "4"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648765536" then
                    third = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648762863" then
                    third = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648759883" then
                    third = "9"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648755440" then
                    third = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648752438" then
                    third = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648749145" then
                    third = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648745618" then
                    third = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648742013" then
                    third = "7"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648738553" then
                    third = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648734698" then
                    third = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648730082" then
                    third = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648723237" then
                    third = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648718450" then
                    third = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648715920" then
                    third = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648712563" then
                    third = "2"
                end
                    end
                end
for i,v in pairs(game.Workspace.Map.CodeBrick.SurfaceGui:GetChildren()) do
                    if v.Name == "4th" then
                        if v.Image == "http://www.roblox.com/asset/?id=9648769161" then
                    fourth = "4"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648765536" then
                    fourth = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648762863" then
                    fourth = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648759883" then
                    fourth = "9"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648755440" then
                    fourth = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648752438" then
                    fourth = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648749145" then
                    fourth = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648745618" then
                    fourth = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648742013" then
                    fourth = "7"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648738553" then
                    fourth = "8"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648734698" then
                    fourth = "2"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648730082" then
                    fourth = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648723237" then
                    fourth = "3"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648718450" then
                    fourth = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648715920" then
                    fourth = "6"
                elseif v.Image == "http://www.roblox.com/asset/?id=9648712563" then
                    fourth = "2"
                end
                    end
                end
CodeEsp = first..second..third..fourth
OrionLib:MakeNotification({Name = "You have code [ "..CodeEsp.." ]",Content = "",Image = "rbxassetid://7733919105",Time = 5})
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons.Reset.ClickDetector)
wait(0.25)
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons[first].ClickDetector)
wait(0.25)
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons[second].ClickDetector)
wait(0.25)
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons[third].ClickDetector)
wait(0.25)
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons[fourth].ClickDetector)
wait(0.25)
fireclickdetector(game.Workspace.Map.OriginOffice.Door.Keypad.Buttons.Enter.ClickDetector)
    end
})

Tab2:AddButton({
	Name = "Получить все ресы",
	Callback = function()
    local orig = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
      		for i, v in ipairs(game.Workspace.Items:GetChildren()) do
                game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = v.Handle.CFrame
                v.Handle.Anchored = true
                wait(0.5)
                Press()
                wait(1.3)
            end
    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = orig
  	end    
})

Tab2:AddButton({
	Name = "Использовать все предметы",
	Callback = function()
		-- Сначала ищем True Power и используем его, если есть
		local backpack = game.Players.LocalPlayer.Backpack
		local character = game.Players.LocalPlayer.Character
		
		-- Проверяем наличие True Power в инвентаре
		local truePowerTool = backpack:FindFirstChild("True Power") or character:FindFirstChild("True Power")
		
		if truePowerTool then
			-- Если True Power в рюкзаке, экипируем его
			if truePowerTool.Parent == backpack then
				game.Players.LocalPlayer.Character.Humanoid:EquipTool(truePowerTool)
			end
			
			-- Активируем True Power
			truePowerTool:Activate()
			wait(0.3)
		end
		
		-- Затем используем все остальные предметы
		for _, item in pairs(backpack:GetChildren()) do
			if item:IsA("Tool") and item.Name ~= "True Power" then
				game.Players.LocalPlayer.Character.Humanoid:EquipTool(item)
				item:Activate()
			end
		end
	end    
})

Tab2:AddSlider({
	Name = "Дальность слап ауры",
	Min = 10,
	Max = 50,
	Default = 25,
	Color = Color3.fromRGB(140, 185, 255),
	Increment = 1,
	ValueName = "Reach",
	Callback = function(Value)
		ReachAura = Value
	end    
})

Tab2:AddToggle({
	Name = "Слап Аура",
	Default = false,
	Callback = function(Value)
		SlapAura = Value
                while SlapAura do
pcall(function()
for i,v in pairs(game.Players:GetChildren()) do
                    if v ~= game.Players.LocalPlayer and v.Character then
if v.Character:FindFirstChild("Dead") == nil and v.Character:FindFirstChild("HumanoidRootPart") and v.Character:WaitForChild("inMatch").Value == true and game.Players.LocalPlayer.Character:WaitForChild("inMatch").Value == true then
Magnitude = (game.Players.LocalPlayer.Character.HumanoidRootPart.Position - v.Character.HumanoidRootPart.Position).Magnitude
                        if ReachAura >= Magnitude then
game.ReplicatedStorage.Events.Slap:FireServer(v.Character:WaitForChild("HumanoidRootPart"))
                    end
end
end
                end
end)
task.wait()
end
	end    
})

local Tab3 = Window:MakeTab({
	Name = "Выборочный лут",
	Icon = "rbxassetid://4483345998",
	PremiumOnly = false
})

local Players = game:GetService("Players")
local Player = Players.LocalPlayer
local Character = Player.Character or Player.CharacterAdded:Wait()
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

local ItemsFolder = game.Workspace.Items
if not ItemsFolder then
    error("Папка 'Items' не найдена!")
end

-- Таблица перевода (англ -> русский)
local itemTranslations = {
    ["Cube of Ice"] = "Ледяной куб",
    ["Apple"] = "Яблоко",
    ["Healing Potion"] = "Зелье лечения",
    ["Bull's essence"] = "Эссенция быка",
    ["Bandage"] = "Бинт",
    ["Frog Potion"] = "Зелье лягушки",
    ["Sphere of fury"] = "Сфера ярости",
    ["Potion of Strength"] = "Зелье силы",
    ["First Aid Kit"] = "Аптечка",
    ["Bomb"] = "Бомба",
    ["True Power"] = "Истинная сила",
    ["Speed Potion"] = "Зелье скорости",
    ["Lightning Potion"] = "Зелье молнии",
    ["Boba"] = "Боба"
}

-- Обратная таблица (русский -> англ)
local reverseTranslations = {}
for eng, rus in pairs(itemTranslations) do
    reverseTranslations[rus] = eng
end

-- Подготовка списка для dropdown
local russianOptions = {}
for _, rusName in pairs(itemTranslations) do
    table.insert(russianOptions, rusName)
end

-- Создаём 3 dropdown
local selectedItems = {}
local dropdowns = {}

for i = 1, 5 do
    dropdowns[i] = Tab3:AddDropdown({
        Name = "Предмет " .. i,
        Default = russianOptions[1],
        Options = russianOptions,
        Callback = function(Value)
            selectedItems[i] = reverseTranslations[Value]
        end
    })
end

-- Тоггл для сбора
local isCollecting = false
local originalCFrame = nil

Tab3:AddToggle({
    Name = "Собирать выбранные предметы",
    Default = false,
    Callback = function(Value)
        isCollecting = Value
        if Value then
            originalCFrame = HumanoidRootPart.CFrame
            task.spawn(function()
                while isCollecting do
                    local foundAny = false
                    for _, item in ipairs(ItemsFolder:GetChildren()) do
                        if not isCollecting then break end
                        
                        for _, selectedName in pairs(selectedItems) do
                            if selectedName and item.Name == selectedName then
                                foundAny = true
                                HumanoidRootPart.CFrame = item.Handle.CFrame
                                item.Handle.Anchored = true
                                task.wait(0.5)
                                game.ReplicatedStorage.Events.Item:FireServer(item.Handle)
                                task.wait(1.3)
                                break
                            end
                        end
                    end
                    
                    if not foundAny then
                        isCollecting = false
                        break
                    end
                end
                
                if originalCFrame then
                    HumanoidRootPart.CFrame = originalCFrame
                end
            end)
        elseif originalCFrame then
            HumanoidRootPart.CFrame = originalCFrame
        end
    end
})

-- Создаем выпадающий список
local realtimeDropdown = Tab3:AddDropdown({
    Name = "📌 Быстрый сбор (реал-тайм)",
    Default = "Сканирую предметы...",
    Options = {"Сканирую предметы..."},
    Callback = function(selectedRussianName)
        local selectedItemName = reverseTranslations[selectedRussianName]
        if not selectedItemName then return end

        -- Ищем предмет в Workspace (только с Handle)
        local targetItem
        for _, item in pairs(game.Workspace.Items:GetChildren()) do
            if item.Name == selectedItemName and item:FindFirstChild("Handle") then
                targetItem = item
                break
            end
        end

        if not targetItem then
            OrionLib:MakeNotification({
                Name = "Ошибка",
                Content = "Предмет уже исчез!",
                Image = "rbxassetid://7733658504",
                Time = 3
            })
            return
        end

        -- Телепортация + сбор
        local originalCFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = targetItem.Handle.CFrame
        targetItem.Handle.Anchored = true
        task.wait(0.25)
        game.ReplicatedStorage.Events.Item:FireServer(targetItem.Handle) -- Ваша функция нажатия F
        task.wait(0.5)
        game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = originalCFrame

        OrionLib:MakeNotification({
            Name = "Успех!",
            Content = "Подобран: "..selectedRussianName,
            Image = "rbxassetid://7733919105",
            Time = 3
        })
    end
})

-- Функция обновления (теперь с полной пересборкой списка)
local function updateRealtimeItems()
    local currentItems = {}
    local addedItems = {} -- Для отслеживания дубликатов

    -- Сканируем только актуальные предметы
    for _, item in pairs(game.Workspace.Items:GetChildren()) do
        if item:FindFirstChild("Handle") then
            local russianName = itemTranslations[item.Name] or item.Name
            if not addedItems[russianName] then -- Исключаем повторы
                table.insert(currentItems, russianName)
                addedItems[russianName] = true
            end
        end
    end

    -- Полностью перезагружаем список
    if #currentItems > 0 then
        realtimeDropdown:Refresh(currentItems, true) -- true = удалить старые варианты
    else
        realtimeDropdown:Refresh({"Нет предметов"}, true)
    end
end

-- Автообновление с интервалом 2 сек (можно изменить)
task.spawn(function()
    while task.wait(1) do -- Более частая проверка
        pcall(updateRealtimeItems) -- Защита от ошибок
    end
end)

-- Первый запуск
updateRealtimeItems()
