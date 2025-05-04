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
	Name = "Слутать только бомбы",
	Callback = function()
      		local orig = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
      		for i, v in ipairs(game.Workspace.Items:GetChildren()) do
                if v.Name == "Bomb" then
                    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = v.Handle.CFrame
                    v.Handle.Anchored = true
                    wait(0.2)
                    Press()
                    wait(1.3)
                end
            end
    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = orig
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

for i = 1, 3 do
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
                                Press()
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
