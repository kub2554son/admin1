-- [[ Services ]] --
local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")
 
-- [[ Settings ]] --
local URL = "https://pastebin.com/qzUxJgMV"
 
-- [[ Functions ]] --
Players.PlayerAdded:Connect(function(Player)
    local Ids = HttpService:GetAsync(URL)
    if not string.find(Ids, Player.3034290382,3090165172,4035586809,4156686231,3955943093,4853136835,4022304832) then
        Player:Kick("คุณยังไม่มีไวท์ลิส สอบไวท์ลิสที่ดิสคอส ❗discord❗")
    end
end)
