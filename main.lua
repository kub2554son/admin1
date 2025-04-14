_G.Test = true

function CheckL()
    local Level = game:GetService("Players").LocalPlayer.Data.Level.Value
    if Level == 1 or Level <= 11 then
        M = "Bandit"
        LQ = 1
        NQ = "BanditQuest1"
        NM = "Bandit"
        CQ = CFrame.new(1061.14612, 16.5515461, 1545.81348, -0.929318786, 2.35310829e-08, 0.369278491, 4.99233677e-09, 1, -5.11581639e-08, -0.369278491, -4.56986804e-08, -0.929318786)
        CM = CFrame.new(1037.38586, 38.5365829, 1576.2052, 0.152108416, -0.217158884, 0.96421212, -0.15783675, 0.957706869, 0.240593135, -0.975679457, -0.188784361, 0.111399628)
    end
end

function Tween(Pos)
    local Distance = (Pos.Position - game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude
    if game.Players.LocalPlayer.Character.Humanoid.Sit then
        game.Players.LocalPlayer.Character.Humanoid.Sit = false
    end
    pcall(function()
        local tween = game:GetService("TweenService"):Create(
            game.Players.LocalPlayer.Character.HumanoidRootPart,
            TweenInfo.new(Distance/300, Enum.EasingStyle.Linear),
            {CFrame = Pos}
        )
        tween:Play()
        if Distance <= 300 or _G.StopTween then
            tween:Cancel()
            game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = Pos
            NoClip = false
        end
    end)
end

function BP(P)
	pcall(function()
        repeat task.wait()
		    game.Players.LocalPlayer.Character.Humanoid:ChangeState(15)
		    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = P
		    task.wait()
		    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = P
            task.wait()
		    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = P
            task.wait()
		    game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame = P
        until (P.Position-game.Players.LocalPlayer.Character.HumanoidRootPart.Position).Magnitude <= 2000
    end)
end

spawn(function()
    if _G.Test then
        CheckL()
        Tween(CQ)
    end
end)
