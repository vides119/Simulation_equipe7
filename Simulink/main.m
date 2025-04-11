classdef main < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                        matlab.ui.Figure
        FichiersMenu                    matlab.ui.container.Menu
        SauvegarderparamtresMenu        matlab.ui.container.Menu
        ChargerparamtresMenu            matlab.ui.container.Menu
        IdentificationMenu              matlab.ui.container.Menu
        IdentifierpropagationMenu       matlab.ui.container.Menu
        IdentifierperturbationMenu      matlab.ui.container.Menu
        GridLayout                      matlab.ui.container.GridLayout
        TabGroup2                       matlab.ui.container.TabGroup
        SignauxTab                      matlab.ui.container.Tab
        GridLayout13                    matlab.ui.container.GridLayout
        Tree                            matlab.ui.container.CheckBoxTree
        RsistancesNode                  matlab.ui.container.TreeNode
        R_T1Node                        matlab.ui.container.TreeNode
        R_T2Node                        matlab.ui.container.TreeNode
        R_T3Node                        matlab.ui.container.TreeNode
        TensionsNode                    matlab.ui.container.TreeNode
        V_T1Node                        matlab.ui.container.TreeNode
        V_T2Node                        matlab.ui.container.TreeNode
        V_T3Node                        matlab.ui.container.TreeNode
        TempraturesNode                 matlab.ui.container.TreeNode
        T1Node                          matlab.ui.container.TreeNode
        T2Node                          matlab.ui.container.TreeNode
        T3Node                          matlab.ui.container.TreeNode
        PRED_T3Node                     matlab.ui.container.TreeNode
        AutresNode                      matlab.ui.container.TreeNode
        CONSIGNENode                    matlab.ui.container.TreeNode
        CMDNode                         matlab.ui.container.TreeNode
        PID_INNode                      matlab.ui.container.TreeNode
        PID_OUTNode                     matlab.ui.container.TreeNode
        PWM_OUTNode                     matlab.ui.container.TreeNode
        AMP_INNode                      matlab.ui.container.TreeNode
        AMP_OUTNode                     matlab.ui.container.TreeNode
        PERTURBNode                     matlab.ui.container.TreeNode
        CommandeTab                     matlab.ui.container.Tab
        GridLayout7                     matlab.ui.container.GridLayout
        CommandePanel                   matlab.ui.container.Panel
        GridLayout14_2                  matlab.ui.container.GridLayout
        UITable_2                       matlab.ui.control.Table
        PerturbationPanel               matlab.ui.container.Panel
        GridLayout10                    matlab.ui.container.GridLayout
        GridLayout11                    matlab.ui.container.GridLayout
        TempschelonsEditField           matlab.ui.control.NumericEditField
        TempschelonsEditFieldLabel      matlab.ui.control.Label
        Switch                          matlab.ui.control.Switch
        GridLayout8                     matlab.ui.container.GridLayout
        DmarrerButton                   matlab.ui.control.Button
        GridLayout9                     matlab.ui.container.GridLayout
        DuresEditField                  matlab.ui.control.NumericEditField
        DuresEditFieldLabel             matlab.ui.control.Label
        ConsigneTab                     matlab.ui.container.Tab
        GridLayout7_2                   matlab.ui.container.GridLayout
        PerturbationPanel_2             matlab.ui.container.Panel
        GridLayout10_2                  matlab.ui.container.GridLayout
        GridLayout11_2                  matlab.ui.container.GridLayout
        TempschelonsEditField_4         matlab.ui.control.NumericEditField
        TempschelonsEditField_4Label    matlab.ui.control.Label
        Switch_2                        matlab.ui.control.Switch
        ConsignePanel                   matlab.ui.container.Panel
        GridLayout14                    matlab.ui.container.GridLayout
        UITable                         matlab.ui.control.Table
        GridLayout8_2                   matlab.ui.container.GridLayout
        Asserviravecprdictiont3CheckBox  matlab.ui.control.CheckBox
        DmarrerButton_2                 matlab.ui.control.Button
        GridLayout9_2                   matlab.ui.container.GridLayout
        DuresEditField_2                matlab.ui.control.NumericEditField
        DuresEditField_2Label           matlab.ui.control.Label
        TabGroup                        matlab.ui.container.TabGroup
        GnralTab                        matlab.ui.container.Tab
        GridLayout2                     matlab.ui.container.GridLayout
        Label                           matlab.ui.control.Label
        GridLayout3                     matlab.ui.container.GridLayout
        TempratureambiantedegCEditField  matlab.ui.control.NumericEditField
        TempratureambiantedegCEditFieldLabel  matlab.ui.control.Label
        PriodechantillonnagesEditField  matlab.ui.control.NumericEditField
        PriodechantillonnagesEditFieldLabel  matlab.ui.control.Label
        RgulateurTab                    matlab.ui.container.Tab
        GridLayout2_2                   matlab.ui.container.GridLayout
        LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel  matlab.ui.control.Label
        GridLayout3_2                   matlab.ui.container.GridLayout
        FrquencecoupureradsEditField    matlab.ui.control.NumericEditField
        FrquencecoupureradsEditFieldLabel  matlab.ui.control.Label
        GaindriveEditField              matlab.ui.control.NumericEditField
        GaindriveEditFieldLabel         matlab.ui.control.Label
        GainintgraleEditField           matlab.ui.control.NumericEditField
        GainintgraleEditFieldLabel      matlab.ui.control.Label
        GainproportionnelEditField      matlab.ui.control.NumericEditField
        GainproportionnelEditFieldLabel  matlab.ui.control.Label
        GainglobalcontrleurEditField    matlab.ui.control.NumericEditField
        GainglobalcontrleurEditFieldLabel  matlab.ui.control.Label
        FTpropagationTab                matlab.ui.container.Tab
        GridLayout2_4                   matlab.ui.container.GridLayout
        T2T3Panel                       matlab.ui.container.Panel
        GridLayout6_7                   matlab.ui.container.GridLayout
        RetardEditField_3               matlab.ui.control.NumericEditField
        RetardEditField_3Label          matlab.ui.control.Label
        TausEditField_8                 matlab.ui.control.NumericEditField
        TausEditField_8Label            matlab.ui.control.Label
        GainDCEditField_8               matlab.ui.control.NumericEditField
        GainDCEditField_8Label          matlab.ui.control.Label
        T1T2Panel                       matlab.ui.container.Panel
        GridLayout6_6                   matlab.ui.container.GridLayout
        RetardEditField_2               matlab.ui.control.NumericEditField
        RetardEditField_2Label          matlab.ui.control.Label
        TausEditField_7                 matlab.ui.control.NumericEditField
        TausEditField_7Label            matlab.ui.control.Label
        GainDCEditField_7               matlab.ui.control.NumericEditField
        GainDCEditField_7Label          matlab.ui.control.Label
        PT1Panel                        matlab.ui.container.Panel
        GridLayout6                     matlab.ui.container.GridLayout
        RetardEditField                 matlab.ui.control.NumericEditField
        RetardEditFieldLabel            matlab.ui.control.Label
        TausEditField_6                 matlab.ui.control.NumericEditField
        TausEditField_6Label            matlab.ui.control.Label
        GainDCEditField_6               matlab.ui.control.NumericEditField
        GainDCEditField_11Label         matlab.ui.control.Label
        LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3  matlab.ui.control.Label
        FTperturbationTab               matlab.ui.container.Tab
        GridLayout2_5                   matlab.ui.container.GridLayout
        PerturbationT2Panel             matlab.ui.container.Panel
        GridLayout6_9                   matlab.ui.container.GridLayout
        RetardEditField_5               matlab.ui.control.NumericEditField
        RetardEditField_5Label          matlab.ui.control.Label
        TausEditField_10                matlab.ui.control.NumericEditField
        TausEditField_10Label           matlab.ui.control.Label
        GainDCEditField_10              matlab.ui.control.NumericEditField
        GainDCEditField_10Label         matlab.ui.control.Label
        PerturbationT1Panel             matlab.ui.container.Panel
        GridLayout6_8                   matlab.ui.container.GridLayout
        RetardEditField_4               matlab.ui.control.NumericEditField
        RetardEditField_4Label          matlab.ui.control.Label
        TausEditField_9                 matlab.ui.control.NumericEditField
        TausEditField_9Label            matlab.ui.control.Label
        GainDCEditField_9               matlab.ui.control.NumericEditField
        GainDCEditField_9Label          matlab.ui.control.Label
        LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4  matlab.ui.control.Label
        GainslectroniqueTab             matlab.ui.container.Tab
        GridLayout2_3                   matlab.ui.container.GridLayout
        GridLayout3_5                   matlab.ui.container.GridLayout
        TaufiltreT3EditField            matlab.ui.control.NumericEditField
        TaufiltreT3EditFieldLabel       matlab.ui.control.Label
        TaufiltreT2EditField            matlab.ui.control.NumericEditField
        TaufiltreT2EditFieldLabel       matlab.ui.control.Label
        TaufiltreT1EditField            matlab.ui.control.NumericEditField
        TaufiltreT1EditFieldLabel       matlab.ui.control.Label
        GridLayout3_4                   matlab.ui.container.GridLayout
        GainampliT3EditField            matlab.ui.control.NumericEditField
        GainampliT3EditFieldLabel       matlab.ui.control.Label
        GainampliT2EditField            matlab.ui.control.NumericEditField
        GainampliT2EditFieldLabel       matlab.ui.control.Label
        GainampliT1EditField            matlab.ui.control.NumericEditField
        GainampliT1EditFieldLabel       matlab.ui.control.Label
        GainamplicommandeEditField      matlab.ui.control.NumericEditField
        GainamplicommandeEditFieldLabel  matlab.ui.control.Label
        OffsetamplicommandeEditField    matlab.ui.control.NumericEditField
        OffsetamplicommandeEditFieldLabel  matlab.ui.control.Label
        LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2  matlab.ui.control.Label
        GridLayout3_3                   matlab.ui.container.GridLayout
        OffsetampliT3EditField          matlab.ui.control.NumericEditField
        OffsetampliT3EditFieldLabel     matlab.ui.control.Label
        OffsetampliT2EditField          matlab.ui.control.NumericEditField
        OffsetampliT2EditFieldLabel     matlab.ui.control.Label
        OffsetampliT1EditField          matlab.ui.control.NumericEditField
        OffsetampliT1EditFieldLabel     matlab.ui.control.Label
        NbrbitsDACEditField             matlab.ui.control.NumericEditField
        NbrbitsDACEditFieldLabel        matlab.ui.control.Label
        NbrbitsADCEditField             matlab.ui.control.NumericEditField
        NbrbitsADCEditFieldLabel        matlab.ui.control.Label
        ThermistancesTab                matlab.ui.container.Tab
        GridLayout15                    matlab.ui.container.GridLayout
        Label_2                         matlab.ui.control.Label
        GridLayout16_2                  matlab.ui.container.GridLayout
        dEditField                      matlab.ui.control.NumericEditField
        dEditFieldLabel                 matlab.ui.control.Label
        cEditField                      matlab.ui.control.NumericEditField
        cEditFieldLabel                 matlab.ui.control.Label
        bEditField                      matlab.ui.control.NumericEditField
        bEditFieldLabel                 matlab.ui.control.Label
        aEditField                      matlab.ui.control.NumericEditField
        aEditFieldLabel                 matlab.ui.control.Label
        GridLayout16                    matlab.ui.container.GridLayout
        DEditField                      matlab.ui.control.NumericEditField
        DEditFieldLabel                 matlab.ui.control.Label
        CEditField                      matlab.ui.control.NumericEditField
        CEditFieldLabel                 matlab.ui.control.Label
        BEditField                      matlab.ui.control.NumericEditField
        BEditFieldLabel                 matlab.ui.control.Label
        AEditField                      matlab.ui.control.NumericEditField
        AEditFieldLabel                 matlab.ui.control.Label
        UIAxes                          matlab.ui.control.UIAxes
        ContextMenu                     matlab.ui.container.ContextMenu
        AjouterMenu_2                   matlab.ui.container.Menu
        ContextMenu2                    matlab.ui.container.ContextMenu
        AjouterMenu                     matlab.ui.container.Menu
    end

    
    methods (Access = private)
        
        function load_sim_params(app)
            assignin("base", "sample_time", app.PriodechantillonnagesEditField.Value);
            assignin("base", "T_ambiant", app.TempratureambiantedegCEditField.Value);

            Gain_controleur = app.GainglobalcontrleurEditField.Value;
            assignin("base", "Gain_controleur", app.GainglobalcontrleurEditField.Value);
            assignin("base", "P", Gain_controleur*app.GainproportionnelEditField.Value);
            assignin("base", "I", Gain_controleur*app.GainintgraleEditField.Value);
            assignin("base", "D", Gain_controleur*app.GaindriveEditField.Value);
            assignin("base", "N", app.FrquencecoupureradsEditField.Value);

            assignin("base", "K1", app.GainDCEditField_6.Value);
            assignin("base", "tau1", app.TausEditField_6.Value);
            assignin("base", "R1", app.RetardEditField.Value);
            assignin("base", "K12", app.GainDCEditField_7.Value);
            assignin("base", "tau12", app.TausEditField_7.Value);
            assignin("base", "R12", app.RetardEditField_2.Value);
            assignin("base", "K23", app.GainDCEditField_8.Value);
            assignin("base", "tau23", app.TausEditField_8.Value);
            assignin("base", "R23", app.RetardEditField_3.Value);

            assignin("base", "Kp1", app.GainDCEditField_9.Value);
            assignin("base", "taup1", app.TausEditField_9.Value);
            assignin("base", "Rp1", app.RetardEditField_4.Value);
            assignin("base", "Kp2", app.GainDCEditField_10.Value);
            assignin("base", "taup2", app.TausEditField_10.Value);
            assignin("base", "Rp2", app.RetardEditField_5.Value);

            assignin("base", "bits_ADC", app.NbrbitsADCEditField.Value);
            assignin("base", "bits_DAC", app.NbrbitsDACEditField.Value);
            assignin("base", "offset_t1", app.OffsetampliT1EditField.Value);
            assignin("base", "offset_t2", app.OffsetampliT2EditField.Value);
            assignin("base", "offset_t3", app.OffsetampliT3EditField.Value);
            assignin("base", "gain_t1", app.GainampliT1EditField.Value);
            assignin("base", "gain_t2", app.GainampliT2EditField.Value);
            assignin("base", "gain_t3", app.GainampliT3EditField.Value);
            assignin("base", "offset_cmd", app.OffsetamplicommandeEditField.Value);
            assignin("base", "gain_cmd", app.GainamplicommandeEditField.Value);
            assignin("base", "tau_f1", app.TaufiltreT1EditField.Value);
            assignin("base", "tau_f2", app.TaufiltreT2EditField.Value);
            assignin("base", "tau_f3", app.TaufiltreT3EditField.Value);

            assignin("base", "cA", app.AEditField.Value);
            assignin("base", "cB", app.BEditField.Value);
            assignin("base", "cC", app.CEditField.Value);
            assignin("base", "cD", app.DEditField.Value);
            assignin("base", "ca", app.aEditField.Value);
            assignin("base", "cb", app.bEditField.Value);
            assignin("base", "cc", app.cEditField.Value);
            assignin("base", "cd", app.dEditField.Value);
        end
    end
    
    methods (Access = private)
        
        function load_cmd_params(app)
            assignin("base", "pert_state", app.Switch.Value)
            assignin("base", "pert_step", app.TempschelonsEditField.Value)
            sorted_rows = sortrows(app.UITable_2.Data, 1);
            cmd = [0 0];
            for k = 1:size(sorted_rows, 1)
                cmd(end+1:end+3, :) = [sorted_rows(k, 1) cmd(end, 2);
                                       sorted_rows(k, 1) sorted_rows(k, 2);
                                       sorted_rows(k, 1) sorted_rows(k, 2)];
            end

            assignin("base", "asserv_t3", app.Asserviravecprdictiont3CheckBox.Value);
            assignin("base", "cmd", cmd);
            assignin("base", "consigne", [25 25]);
        end
    end

    methods (Access = private)
        
        function load_consigne_params(app)
            assignin("base", "pert_state", app.Switch_2.Value)
            assignin("base", "pert_step", app.TempschelonsEditField_4.Value)
            sorted_rows = sortrows(app.UITable.Data, 1);
            consigne = [0 0];
            for k = 1:size(sorted_rows, 1)
                consigne(end+1:end+3, :) = [sorted_rows(k, 1) consigne(end, 2);
                                       sorted_rows(k, 1) sorted_rows(k, 2);
                                       sorted_rows(k, 1) sorted_rows(k, 2)];
            end
            assignin("base", "asserv_t3", app.Asserviravecprdictiont3CheckBox.Value);
            assignin("base", "consigne", consigne);
            assignin("base", "cmd", [0 0]);
        end
    end

    methods (Access = private)

        function signals = get_chosen_signals(app)
            checked = app.Tree.CheckedNodes;
            signals =  string(arrayfun(@(n) n.NodeData, checked, 'UniformOutput', false));
            signals = signals(signals ~= "None");
        end
    end

    methods (Access = public)
        function saveVarsToJSON(app, varNames, filename)
            % Save selected workspace variables to a JSON file
            % varNames: string array or cell array of variable names (as text)
            % filename: output JSON file path (e.g. 'myData.json')
        
            if isstring(varNames)
                varNames = cellstr(varNames);  % convert to cell array of chars
            end
        
            dataStruct = struct();
        
            for i = 1:numel(varNames)
                name = varNames{i};
        
                try
                    % Get the variable from the base workspace
                    value = evalin('base', name);
                    dataStruct.(name) = value;
                catch
                    warning("Variable '%s' not found in base workspace.", name);
                end
            end
        
            % Convert to JSON and write to file
            jsonStr = jsonencode(dataStruct);
        
            % Optional: make JSON pretty (add newlines/indents)
            %jsonStr = prettyJson(jsonStr);
        
            fid = fopen(filename, 'w');
            if fid == -1
                error("Could not open file: %s", filename);
            end
            fwrite(fid, jsonStr, 'char');
            fclose(fid);
        end
    end

    methods (Access = public)
        function loadVarsFromJSON(app, filename)
            % Load variables from a JSON file and assign them to the base workspace
            % Each field in the JSON becomes a variable with the same name
        
            if ~isfile(filename)
                error("File not found: %s", filename);
            end
        
            % Read the JSON file as text
            jsonText = fileread(filename);
        
            % Decode into a struct
            data = jsondecode(jsonText);
        
            % Assign each field into the base workspace
            varNames = fieldnames(data);
            for i = 1:numel(varNames)
                name = varNames{i};
                value = data.(name);
                assignin('base', name, value);
            end
        end
    end

    methods (Access = private)
        function [K, tau, retard, sys] = ident_tf(app, t, u, y)
            y = y-y(1); %retire pt opération
            Ts = t(2) - t(1);  % sample time
            data = iddata(y, u, Ts);
            
            % 2. Estimate the transfer function (e.g., 2 poles, 1 zero)
            sys = tfest(data, 1, 0);
            [num, den] = tfdata(sys, 'v');
            normVal = den(2);
            num = num/normVal;
            den = den/normVal;
            K = num(end);
            tau = den(1);
            retard = sys.InputDelay;
        end
    end
    

    % Callbacks that handle component events
    methods (Access = private)

        % Code that executes after component creation
        function Init(app)
            app.UITable.Data = [0, 24];
            app.UITable_2.Data = [0, 0];
            msgbox(["Bonjour! Bienvenue dans l'interface de la simulation d'asservissement"; ...
                    "Pour de l'aide avec les paramètres/boutons, faites flotter la souris au dessus de l'élément."]);
        end

        % Button pushed function: DmarrerButton
        function DmarrerButtonPushed(app, event)
           %fonction démarrer COMMANDE
           load_sim_params(app);
           load_cmd_params(app);
           assignin("base", "mode", 1)
           out = sim("Asservissement_2023a.slx", "StopTime", num2str(app.DuresEditField.Value));

           signals = get_chosen_signals(app);
          
           cla(app.UIAxes, "reset");
           hold(app.UIAxes, "on");
           for k = 1:length(signals)
                sig = eval("out."+signals(k));
                plot(app.UIAxes, sig.Time, sig.Data);
           end
           legend(app.UIAxes, signals);
        end

        % Button pushed function: DmarrerButton_2
        function Start_consigne(app, event)
            %fonction démarrer CONSIGNE
           load_sim_params(app);
           load_consigne_params(app);
           assignin("base", "mode", 0)
           out = sim("Asservissement_2023a.slx", "StopTime", num2str(app.DuresEditField_2.Value));

           signals = get_chosen_signals(app);
          
           cla(app.UIAxes, "reset");
           hold(app.UIAxes, "on");
           for k = 1:length(signals)
                sig = eval("out."+signals(k));
                plot(app.UIAxes, sig.Time, sig.Data);
           end
           legend(app.UIAxes, signals);
        end

        % Menu selected function: AjouterMenu_2
        function Add_row_consigne(app, event)
         
            app.UITable.Data = [app.UITable.Data; 0 0];
        end

        % Menu selected function: AjouterMenu
        function Add_row_commande(app, event)
            app.UITable_2.Data = [app.UITable_2.Data; 0 0];
        end

        % Menu selected function: SauvegarderparamtresMenu
        function save_params(app, event)
            [file, location, indx] = uiputfile("params.json");
            load_sim_params(app);
            vars = ["sample_time", "T_ambiant", "Gain_controleur", "P", "I", "D", "N", "K1", "tau1", "R1", "K12", "tau12", "R12", "K23", "tau23", "R23", "Kp1", "taup1", "Rp1", "Kp2", "taup2", "Rp2", "bits_ADC", "bits_DAC", "offset_t1", "offset_t2", "offset_t3", "gain_t1", "gain_t2", "gain_t3", "offset_cmd", "gain_cmd", "cA", "cB", "cC", "cD", "ca", "cb", "cc", "cd", "tau_f1", "tau_f2", "tau_f3"];
            saveVarsToJSON(app, vars, file);
        end

        % Menu selected function: ChargerparamtresMenu
        function charge_params(app, event)
            [file, location] = uigetfile("*.json");
            loadVarsFromJSON(app, file);
            app.PriodechantillonnagesEditField.Value = evalin("base", "sample_time");
            app.TempratureambiantedegCEditField.Value = evalin("base", "T_ambiant");
            app.GainglobalcontrleurEditField.Value = evalin("base", "Gain_controleur");
            app.GainproportionnelEditField.Value = evalin("base", "P");
            app.GainintgraleEditField.Value = evalin("base", "I");
            app.GaindriveEditField.Value = evalin("base", "D");
            app.FrquencecoupureradsEditField.Value = evalin("base", "N");
            app.GainDCEditField_6.Value = evalin("base", "K1");
            app.TausEditField_6.Value = evalin("base", "tau1");
            app.RetardEditField.Value = evalin("base", "R1");
            app.GainDCEditField_7.Value = evalin("base", "K12");
            app.TausEditField_7.Value = evalin("base", "tau12");
            app.RetardEditField_2.Value = evalin("base", "R12");
            app.GainDCEditField_8.Value = evalin("base", "K23");
            app.TausEditField_8.Value = evalin("base", "tau23");
            app.RetardEditField_3.Value = evalin("base", "R23");
            app.GainDCEditField_9.Value = evalin("base", "Kp1");
            app.TausEditField_9.Value = evalin("base", "taup1");
            app.RetardEditField_4.Value = evalin("base", "Rp1");
            app.GainDCEditField_10.Value = evalin("base", "Kp2");
            app.TausEditField_10.Value = evalin("base", "taup2");
            app.RetardEditField_5.Value = evalin("base", "Rp2");
            app.NbrbitsADCEditField.Value = evalin("base", "bits_ADC");
            app.NbrbitsDACEditField.Value = evalin("base", "bits_DAC");
            app.OffsetampliT1EditField.Value = evalin("base", "offset_t1");
            app.OffsetampliT2EditField.Value = evalin("base", "offset_t2");
            app.OffsetampliT3EditField.Value = evalin("base", "offset_t3");
            app.GainampliT1EditField.Value = evalin("base", "gain_t1");
            app.GainampliT2EditField.Value = evalin("base", "gain_t2");
            app.GainampliT3EditField.Value = evalin("base", "gain_t3");
            app.OffsetamplicommandeEditField.Value = evalin("base", "offset_cmd");
            app.GainamplicommandeEditField.Value = evalin("base", "gain_cmd");
            app.TaufiltreT1EditField.Value = evalin("base", "tau_f1");
            app.TaufiltreT2EditField.Value = evalin("base", "tau_f2");
            app.TaufiltreT3EditField.Value = evalin("base", "tau_f3");
            app.AEditField.Value = evalin("base", "cA");
            app.BEditField.Value = evalin("base", "cB");
            app.CEditField.Value = evalin("base", "cC");
            app.DEditField.Value = evalin("base", "cD");
            app.aEditField.Value = evalin("base", "ca");
            app.bEditField.Value = evalin("base", "cb");
            app.cEditField.Value = evalin("base", "cc");
            app.dEditField.Value = evalin("base", "cd");
        end

        % Menu selected function: IdentifierpropagationMenu
        function ident_propagation(app, event)
            [file, location] = uigetfile("*.csv");
            data = readmatrix([location file]);
            n = round(0.5/(data(2, 1)-data(1, 1)));
            t = downsample(data(:, 1), n);
            P_cmd = downsample(data(:, 2), n);
            P_pert = downsample(data(:, 3), n);
            t1 = downsample(data(:, 4), n);
            t1 = t1-t1(1);
            t2 = downsample(data(:, 5), n);
            t2 = t2-t2(1);
            t3 = downsample(data(:, 6), n);
            t3 = t3-t3(1);
            [K1, tau1, R1, sys1] = ident_tf(app, t, P_cmd, t1);
            [K12, tau12, R12, sys12] = ident_tf(app, t, t1, t2);
            [K23, tau23, R23, sys23] = ident_tf(app, t, t2, t3);

            app.GainDCEditField_6.Value = K1;
            app.TausEditField_6.Value = tau1;
            app.RetardEditField.Value = R1;
            app.GainDCEditField_7.Value = K12;
            app.TausEditField_7.Value = tau12;
            app.RetardEditField_2.Value = R12;
            app.GainDCEditField_8.Value = K23;
            app.TausEditField_8.Value = tau23;
            app.RetardEditField_3.Value = R23;

            figure;
            hold on;
            plot(t, P_cmd, "k");
            plot(t, t1, "-r");
            t1_fit = lsim(sys1, P_cmd, t);
            plot(t, t1_fit, ":r");
            plot(t, t2, "-b");
            t2_fit = lsim(sys12, t1, t);
            plot(t, t2_fit, ":b");
            plot(t, t3, "-g");
            t3_fit = lsim(sys23, t2, t);
            plot(t, t3_fit, ":g");
            title("Identification des fonctions de transfert de la propagation de la température");
            legend("Puissance", "t1 données", "t1 estimation", "t2 données", "t2 estimation", "t3 données", "t3 estimation");
            xlabel("Temps [s]");
            ylabel("Y");

            msgbox("Paramètres identifiés et mis à jours dans la section paramètres: FT Propagation");
            
        end

        % Menu selected function: IdentifierperturbationMenu
        function identifier_perturbation(app, event)
            [file, location] = uigetfile("*.csv");
            data = readmatrix([location file]);
            n = round(0.5/(data(2, 1)-data(1, 1)));
            t = downsample(data(:, 1), n);
            P_cmd = downsample(data(:, 2), n);
            P_pert = downsample(data(:, 3), n);
            t1 = downsample(data(:, 4), n);
            t1 = t1-t1(1);
            t2 = downsample(data(:, 5), n);
            t2 = t2-t2(1);
            [Kp1, taup1, Rp1, sysp1] = ident_tf(app, t, P_pert, t1);
            [Kp2, taup2, Rp2, sysp2] = ident_tf(app, t, P_pert, t2);

            app.GainDCEditField_9.Value = Kp1;
            app.TausEditField_9.Value = taup1;
            app.RetardEditField_4.Value = Rp1;
            app.GainDCEditField_10.Value = Kp2;
            app.TausEditField_10.Value = taup2;
            app.RetardEditField_5.Value = Rp2;

            figure;
            hold on;
            plot(t, P_pert, "k");
            plot(t, t1, "-r");
            t1_fit = lsim(sysp1, P_pert, t);
            plot(t, t1_fit, ":r");
            plot(t, t2, "-b");
            t2_fit = lsim(sysp2, P_pert, t);
            plot(t, t2_fit, ":b");
            title("Identification des fonctions de transfert de la propagation de la perturbation");
            legend("Puissance", "t1 données", "t1 estimation", "t2 données", "t2 estimation", "t3 données", "t3 estimation");
            xlabel("Temps [s]");
            ylabel("Y");

            msgbox("Paramètres identifiés et mis à jours dans la section paramètres: FT Perturbation");
        end
    end

    % Component initialization
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure and hide until all components are created
            app.UIFigure = uifigure('Visible', 'off');
            app.UIFigure.Position = [100 100 743 720];
            app.UIFigure.Name = 'MATLAB App';

            % Create FichiersMenu
            app.FichiersMenu = uimenu(app.UIFigure);
            app.FichiersMenu.Text = 'Fichiers';

            % Create SauvegarderparamtresMenu
            app.SauvegarderparamtresMenu = uimenu(app.FichiersMenu);
            app.SauvegarderparamtresMenu.MenuSelectedFcn = createCallbackFcn(app, @save_params, true);
            app.SauvegarderparamtresMenu.Text = 'Sauvegarder paramètres';

            % Create ChargerparamtresMenu
            app.ChargerparamtresMenu = uimenu(app.FichiersMenu);
            app.ChargerparamtresMenu.MenuSelectedFcn = createCallbackFcn(app, @charge_params, true);
            app.ChargerparamtresMenu.Text = 'Charger paramètres';

            % Create IdentificationMenu
            app.IdentificationMenu = uimenu(app.UIFigure);
            app.IdentificationMenu.Text = 'Identification';

            % Create IdentifierpropagationMenu
            app.IdentifierpropagationMenu = uimenu(app.IdentificationMenu);
            app.IdentifierpropagationMenu.MenuSelectedFcn = createCallbackFcn(app, @ident_propagation, true);
            app.IdentifierpropagationMenu.Text = 'Identifier propagation';

            % Create IdentifierperturbationMenu
            app.IdentifierperturbationMenu = uimenu(app.IdentificationMenu);
            app.IdentifierperturbationMenu.MenuSelectedFcn = createCallbackFcn(app, @identifier_perturbation, true);
            app.IdentifierperturbationMenu.Text = 'Identifier perturbation';

            % Create GridLayout
            app.GridLayout = uigridlayout(app.UIFigure);
            app.GridLayout.ColumnWidth = {'1x'};
            app.GridLayout.RowHeight = {'1.5x', '1x', '2x'};

            % Create UIAxes
            app.UIAxes = uiaxes(app.GridLayout);
            title(app.UIAxes, 'Signaux')
            xlabel(app.UIAxes, 'Temps [s]')
            ylabel(app.UIAxes, 'Mesure')
            zlabel(app.UIAxes, 'Z')
            app.UIAxes.Layout.Row = 3;
            app.UIAxes.Layout.Column = 1;

            % Create TabGroup
            app.TabGroup = uitabgroup(app.GridLayout);
            app.TabGroup.Tag = 'params_tab';
            app.TabGroup.Layout.Row = 1;
            app.TabGroup.Layout.Column = 1;

            % Create GnralTab
            app.GnralTab = uitab(app.TabGroup);
            app.GnralTab.Tooltip = {''};
            app.GnralTab.Title = 'Général';

            % Create GridLayout2
            app.GridLayout2 = uigridlayout(app.GnralTab);
            app.GridLayout2.ColumnWidth = {'1x', 'fit'};
            app.GridLayout2.RowHeight = {'fit'};

            % Create GridLayout3
            app.GridLayout3 = uigridlayout(app.GridLayout2);
            app.GridLayout3.ColumnWidth = {'fit', '1x'};
            app.GridLayout3.Layout.Row = 1;
            app.GridLayout3.Layout.Column = 2;

            % Create PriodechantillonnagesEditFieldLabel
            app.PriodechantillonnagesEditFieldLabel = uilabel(app.GridLayout3);
            app.PriodechantillonnagesEditFieldLabel.HorizontalAlignment = 'right';
            app.PriodechantillonnagesEditFieldLabel.Layout.Row = 1;
            app.PriodechantillonnagesEditFieldLabel.Layout.Column = 1;
            app.PriodechantillonnagesEditFieldLabel.Text = 'Période échantillonnage [s]';

            % Create PriodechantillonnagesEditField
            app.PriodechantillonnagesEditField = uieditfield(app.GridLayout3, 'numeric');
            app.PriodechantillonnagesEditField.Layout.Row = 1;
            app.PriodechantillonnagesEditField.Layout.Column = 2;
            app.PriodechantillonnagesEditField.Value = 1;

            % Create TempratureambiantedegCEditFieldLabel
            app.TempratureambiantedegCEditFieldLabel = uilabel(app.GridLayout3);
            app.TempratureambiantedegCEditFieldLabel.HorizontalAlignment = 'right';
            app.TempratureambiantedegCEditFieldLabel.Layout.Row = 2;
            app.TempratureambiantedegCEditFieldLabel.Layout.Column = 1;
            app.TempratureambiantedegCEditFieldLabel.Text = 'Température ambiante [deg C]';

            % Create TempratureambiantedegCEditField
            app.TempratureambiantedegCEditField = uieditfield(app.GridLayout3, 'numeric');
            app.TempratureambiantedegCEditField.Layout.Row = 2;
            app.TempratureambiantedegCEditField.Layout.Column = 2;
            app.TempratureambiantedegCEditField.Value = 24;

            % Create Label
            app.Label = uilabel(app.GridLayout2);
            app.Label.WordWrap = 'on';
            app.Label.Layout.Row = 1;
            app.Label.Layout.Column = 1;
            app.Label.Text = 'Les paramètres généraux de la simulation, autant valides autant en mode consigne que commande.';

            % Create RgulateurTab
            app.RgulateurTab = uitab(app.TabGroup);
            app.RgulateurTab.Title = 'Régulateur';

            % Create GridLayout2_2
            app.GridLayout2_2 = uigridlayout(app.RgulateurTab);
            app.GridLayout2_2.ColumnWidth = {'1x', 'fit'};
            app.GridLayout2_2.RowHeight = {'fit'};

            % Create GridLayout3_2
            app.GridLayout3_2 = uigridlayout(app.GridLayout2_2);
            app.GridLayout3_2.ColumnWidth = {'fit', '1x'};
            app.GridLayout3_2.RowHeight = {'1x', '1x', '1x', '1x', '1x'};
            app.GridLayout3_2.Layout.Row = 1;
            app.GridLayout3_2.Layout.Column = 2;

            % Create GainglobalcontrleurEditFieldLabel
            app.GainglobalcontrleurEditFieldLabel = uilabel(app.GridLayout3_2);
            app.GainglobalcontrleurEditFieldLabel.HorizontalAlignment = 'right';
            app.GainglobalcontrleurEditFieldLabel.Layout.Row = 1;
            app.GainglobalcontrleurEditFieldLabel.Layout.Column = 1;
            app.GainglobalcontrleurEditFieldLabel.Text = 'Gain global contrôleur';

            % Create GainglobalcontrleurEditField
            app.GainglobalcontrleurEditField = uieditfield(app.GridLayout3_2, 'numeric');
            app.GainglobalcontrleurEditField.Layout.Row = 1;
            app.GainglobalcontrleurEditField.Layout.Column = 2;
            app.GainglobalcontrleurEditField.Value = 1;

            % Create GainproportionnelEditFieldLabel
            app.GainproportionnelEditFieldLabel = uilabel(app.GridLayout3_2);
            app.GainproportionnelEditFieldLabel.HorizontalAlignment = 'right';
            app.GainproportionnelEditFieldLabel.Layout.Row = 2;
            app.GainproportionnelEditFieldLabel.Layout.Column = 1;
            app.GainproportionnelEditFieldLabel.Text = 'Gain proportionnel';

            % Create GainproportionnelEditField
            app.GainproportionnelEditField = uieditfield(app.GridLayout3_2, 'numeric');
            app.GainproportionnelEditField.Layout.Row = 2;
            app.GainproportionnelEditField.Layout.Column = 2;
            app.GainproportionnelEditField.Value = 0.2327;

            % Create GainintgraleEditFieldLabel
            app.GainintgraleEditFieldLabel = uilabel(app.GridLayout3_2);
            app.GainintgraleEditFieldLabel.HorizontalAlignment = 'right';
            app.GainintgraleEditFieldLabel.Layout.Row = 3;
            app.GainintgraleEditFieldLabel.Layout.Column = 1;
            app.GainintgraleEditFieldLabel.Text = 'Gain intégrale';

            % Create GainintgraleEditField
            app.GainintgraleEditField = uieditfield(app.GridLayout3_2, 'numeric');
            app.GainintgraleEditField.Layout.Row = 3;
            app.GainintgraleEditField.Layout.Column = 2;
            app.GainintgraleEditField.Value = 0.002;

            % Create GaindriveEditFieldLabel
            app.GaindriveEditFieldLabel = uilabel(app.GridLayout3_2);
            app.GaindriveEditFieldLabel.HorizontalAlignment = 'right';
            app.GaindriveEditFieldLabel.Layout.Row = 4;
            app.GaindriveEditFieldLabel.Layout.Column = 1;
            app.GaindriveEditFieldLabel.Text = 'Gain dérivée';

            % Create GaindriveEditField
            app.GaindriveEditField = uieditfield(app.GridLayout3_2, 'numeric');
            app.GaindriveEditField.Layout.Row = 4;
            app.GaindriveEditField.Layout.Column = 2;
            app.GaindriveEditField.Value = 5;

            % Create FrquencecoupureradsEditFieldLabel
            app.FrquencecoupureradsEditFieldLabel = uilabel(app.GridLayout3_2);
            app.FrquencecoupureradsEditFieldLabel.HorizontalAlignment = 'right';
            app.FrquencecoupureradsEditFieldLabel.Layout.Row = 5;
            app.FrquencecoupureradsEditFieldLabel.Layout.Column = 1;
            app.FrquencecoupureradsEditFieldLabel.Text = 'Fréquence coupure [rad/s]';

            % Create FrquencecoupureradsEditField
            app.FrquencecoupureradsEditField = uieditfield(app.GridLayout3_2, 'numeric');
            app.FrquencecoupureradsEditField.Layout.Row = 5;
            app.FrquencecoupureradsEditField.Layout.Column = 2;
            app.FrquencecoupureradsEditField.Value = 2.668;

            % Create LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel = uilabel(app.GridLayout2_2);
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel.WordWrap = 'on';
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel.Layout.Row = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel.Layout.Column = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel.Text = 'Les paramètres du régulateur. Concernent seulement le mode consigne.';

            % Create FTpropagationTab
            app.FTpropagationTab = uitab(app.TabGroup);
            app.FTpropagationTab.Title = 'FT propagation';

            % Create GridLayout2_4
            app.GridLayout2_4 = uigridlayout(app.FTpropagationTab);
            app.GridLayout2_4.ColumnWidth = {'1x', '1x', '1x', '1x'};
            app.GridLayout2_4.RowHeight = {'1x'};

            % Create LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3 = uilabel(app.GridLayout2_4);
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3.WordWrap = 'on';
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3.Layout.Row = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3.Layout.Column = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_3.Text = 'Les trois fonctions de transfert de la propagation de la température sont des 1er ordres en SÉRIE. Tau correspond à la constante de temps de la fonction de transfert';

            % Create PT1Panel
            app.PT1Panel = uipanel(app.GridLayout2_4);
            app.PT1Panel.Title = 'P -> T1';
            app.PT1Panel.Layout.Row = 1;
            app.PT1Panel.Layout.Column = 2;

            % Create GridLayout6
            app.GridLayout6 = uigridlayout(app.PT1Panel);
            app.GridLayout6.RowHeight = {'fit', 'fit', 'fit'};

            % Create GainDCEditField_11Label
            app.GainDCEditField_11Label = uilabel(app.GridLayout6);
            app.GainDCEditField_11Label.HorizontalAlignment = 'right';
            app.GainDCEditField_11Label.Layout.Row = 1;
            app.GainDCEditField_11Label.Layout.Column = 1;
            app.GainDCEditField_11Label.Text = 'Gain DC';

            % Create GainDCEditField_6
            app.GainDCEditField_6 = uieditfield(app.GridLayout6, 'numeric');
            app.GainDCEditField_6.Layout.Row = 1;
            app.GainDCEditField_6.Layout.Column = 2;
            app.GainDCEditField_6.Value = 10.7;

            % Create TausEditField_6Label
            app.TausEditField_6Label = uilabel(app.GridLayout6);
            app.TausEditField_6Label.HorizontalAlignment = 'right';
            app.TausEditField_6Label.Layout.Row = 2;
            app.TausEditField_6Label.Layout.Column = 1;
            app.TausEditField_6Label.Text = 'Tau [s]';

            % Create TausEditField_6
            app.TausEditField_6 = uieditfield(app.GridLayout6, 'numeric');
            app.TausEditField_6.Layout.Row = 2;
            app.TausEditField_6.Layout.Column = 2;
            app.TausEditField_6.Value = 109.78;

            % Create RetardEditFieldLabel
            app.RetardEditFieldLabel = uilabel(app.GridLayout6);
            app.RetardEditFieldLabel.HorizontalAlignment = 'right';
            app.RetardEditFieldLabel.Layout.Row = 3;
            app.RetardEditFieldLabel.Layout.Column = 1;
            app.RetardEditFieldLabel.Text = 'Retard';

            % Create RetardEditField
            app.RetardEditField = uieditfield(app.GridLayout6, 'numeric');
            app.RetardEditField.Layout.Row = 3;
            app.RetardEditField.Layout.Column = 2;

            % Create T1T2Panel
            app.T1T2Panel = uipanel(app.GridLayout2_4);
            app.T1T2Panel.Title = 'T1 -> T2';
            app.T1T2Panel.Layout.Row = 1;
            app.T1T2Panel.Layout.Column = 3;

            % Create GridLayout6_6
            app.GridLayout6_6 = uigridlayout(app.T1T2Panel);
            app.GridLayout6_6.RowHeight = {'fit', 'fit', 'fit'};

            % Create GainDCEditField_7Label
            app.GainDCEditField_7Label = uilabel(app.GridLayout6_6);
            app.GainDCEditField_7Label.HorizontalAlignment = 'right';
            app.GainDCEditField_7Label.Layout.Row = 1;
            app.GainDCEditField_7Label.Layout.Column = 1;
            app.GainDCEditField_7Label.Text = 'Gain DC';

            % Create GainDCEditField_7
            app.GainDCEditField_7 = uieditfield(app.GridLayout6_6, 'numeric');
            app.GainDCEditField_7.Layout.Row = 1;
            app.GainDCEditField_7.Layout.Column = 2;
            app.GainDCEditField_7.Value = 0.7918;

            % Create TausEditField_7Label
            app.TausEditField_7Label = uilabel(app.GridLayout6_6);
            app.TausEditField_7Label.HorizontalAlignment = 'right';
            app.TausEditField_7Label.Layout.Row = 2;
            app.TausEditField_7Label.Layout.Column = 1;
            app.TausEditField_7Label.Text = 'Tau [s]';

            % Create TausEditField_7
            app.TausEditField_7 = uieditfield(app.GridLayout6_6, 'numeric');
            app.TausEditField_7.Layout.Row = 2;
            app.TausEditField_7.Layout.Column = 2;
            app.TausEditField_7.Value = 43.3;

            % Create RetardEditField_2Label
            app.RetardEditField_2Label = uilabel(app.GridLayout6_6);
            app.RetardEditField_2Label.HorizontalAlignment = 'right';
            app.RetardEditField_2Label.Layout.Row = 3;
            app.RetardEditField_2Label.Layout.Column = 1;
            app.RetardEditField_2Label.Text = 'Retard';

            % Create RetardEditField_2
            app.RetardEditField_2 = uieditfield(app.GridLayout6_6, 'numeric');
            app.RetardEditField_2.Layout.Row = 3;
            app.RetardEditField_2.Layout.Column = 2;

            % Create T2T3Panel
            app.T2T3Panel = uipanel(app.GridLayout2_4);
            app.T2T3Panel.Title = 'T2 -> T3';
            app.T2T3Panel.Layout.Row = 1;
            app.T2T3Panel.Layout.Column = 4;

            % Create GridLayout6_7
            app.GridLayout6_7 = uigridlayout(app.T2T3Panel);
            app.GridLayout6_7.RowHeight = {'fit', 'fit', 'fit'};

            % Create GainDCEditField_8Label
            app.GainDCEditField_8Label = uilabel(app.GridLayout6_7);
            app.GainDCEditField_8Label.HorizontalAlignment = 'right';
            app.GainDCEditField_8Label.Layout.Row = 1;
            app.GainDCEditField_8Label.Layout.Column = 1;
            app.GainDCEditField_8Label.Text = 'Gain DC';

            % Create GainDCEditField_8
            app.GainDCEditField_8 = uieditfield(app.GridLayout6_7, 'numeric');
            app.GainDCEditField_8.Layout.Row = 1;
            app.GainDCEditField_8.Layout.Column = 2;
            app.GainDCEditField_8.Value = 0.8866;

            % Create TausEditField_8Label
            app.TausEditField_8Label = uilabel(app.GridLayout6_7);
            app.TausEditField_8Label.HorizontalAlignment = 'right';
            app.TausEditField_8Label.Layout.Row = 2;
            app.TausEditField_8Label.Layout.Column = 1;
            app.TausEditField_8Label.Text = 'Tau [s]';

            % Create TausEditField_8
            app.TausEditField_8 = uieditfield(app.GridLayout6_7, 'numeric');
            app.TausEditField_8.Layout.Row = 2;
            app.TausEditField_8.Layout.Column = 2;
            app.TausEditField_8.Value = 22.51;

            % Create RetardEditField_3Label
            app.RetardEditField_3Label = uilabel(app.GridLayout6_7);
            app.RetardEditField_3Label.HorizontalAlignment = 'right';
            app.RetardEditField_3Label.Layout.Row = 3;
            app.RetardEditField_3Label.Layout.Column = 1;
            app.RetardEditField_3Label.Text = 'Retard';

            % Create RetardEditField_3
            app.RetardEditField_3 = uieditfield(app.GridLayout6_7, 'numeric');
            app.RetardEditField_3.Layout.Row = 3;
            app.RetardEditField_3.Layout.Column = 2;

            % Create FTperturbationTab
            app.FTperturbationTab = uitab(app.TabGroup);
            app.FTperturbationTab.Title = 'FT perturbation';

            % Create GridLayout2_5
            app.GridLayout2_5 = uigridlayout(app.FTperturbationTab);
            app.GridLayout2_5.ColumnWidth = {'1x', '1x', '1x'};
            app.GridLayout2_5.RowHeight = {'fit'};

            % Create LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4 = uilabel(app.GridLayout2_5);
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4.WordWrap = 'on';
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4.Layout.Row = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4.Layout.Column = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_4.Text = 'Les trois fonctions de transfert de la propagation de la température sont des 1er ordres en SÉRIE. Tau correspond à la constante de temps de la fonction de transfert';

            % Create PerturbationT1Panel
            app.PerturbationT1Panel = uipanel(app.GridLayout2_5);
            app.PerturbationT1Panel.Title = 'Perturbation -> T1';
            app.PerturbationT1Panel.Layout.Row = 1;
            app.PerturbationT1Panel.Layout.Column = 2;

            % Create GridLayout6_8
            app.GridLayout6_8 = uigridlayout(app.PerturbationT1Panel);
            app.GridLayout6_8.RowHeight = {'fit', 'fit', 'fit'};

            % Create GainDCEditField_9Label
            app.GainDCEditField_9Label = uilabel(app.GridLayout6_8);
            app.GainDCEditField_9Label.HorizontalAlignment = 'right';
            app.GainDCEditField_9Label.Layout.Row = 1;
            app.GainDCEditField_9Label.Layout.Column = 1;
            app.GainDCEditField_9Label.Text = 'Gain DC';

            % Create GainDCEditField_9
            app.GainDCEditField_9 = uieditfield(app.GridLayout6_8, 'numeric');
            app.GainDCEditField_9.Layout.Row = 1;
            app.GainDCEditField_9.Layout.Column = 2;
            app.GainDCEditField_9.Value = 4.1129;

            % Create TausEditField_9Label
            app.TausEditField_9Label = uilabel(app.GridLayout6_8);
            app.TausEditField_9Label.HorizontalAlignment = 'right';
            app.TausEditField_9Label.Layout.Row = 2;
            app.TausEditField_9Label.Layout.Column = 1;
            app.TausEditField_9Label.Text = 'Tau [s]';

            % Create TausEditField_9
            app.TausEditField_9 = uieditfield(app.GridLayout6_8, 'numeric');
            app.TausEditField_9.Layout.Row = 2;
            app.TausEditField_9.Layout.Column = 2;
            app.TausEditField_9.Value = 136.85;

            % Create RetardEditField_4Label
            app.RetardEditField_4Label = uilabel(app.GridLayout6_8);
            app.RetardEditField_4Label.HorizontalAlignment = 'right';
            app.RetardEditField_4Label.Layout.Row = 3;
            app.RetardEditField_4Label.Layout.Column = 1;
            app.RetardEditField_4Label.Text = 'Retard';

            % Create RetardEditField_4
            app.RetardEditField_4 = uieditfield(app.GridLayout6_8, 'numeric');
            app.RetardEditField_4.Layout.Row = 3;
            app.RetardEditField_4.Layout.Column = 2;

            % Create PerturbationT2Panel
            app.PerturbationT2Panel = uipanel(app.GridLayout2_5);
            app.PerturbationT2Panel.Title = 'Perturbation -> T2';
            app.PerturbationT2Panel.Layout.Row = 1;
            app.PerturbationT2Panel.Layout.Column = 3;

            % Create GridLayout6_9
            app.GridLayout6_9 = uigridlayout(app.PerturbationT2Panel);
            app.GridLayout6_9.RowHeight = {'fit', 'fit', 'fit'};

            % Create GainDCEditField_10Label
            app.GainDCEditField_10Label = uilabel(app.GridLayout6_9);
            app.GainDCEditField_10Label.HorizontalAlignment = 'right';
            app.GainDCEditField_10Label.Layout.Row = 1;
            app.GainDCEditField_10Label.Layout.Column = 1;
            app.GainDCEditField_10Label.Text = 'Gain DC';

            % Create GainDCEditField_10
            app.GainDCEditField_10 = uieditfield(app.GridLayout6_9, 'numeric');
            app.GainDCEditField_10.Layout.Row = 1;
            app.GainDCEditField_10.Layout.Column = 2;
            app.GainDCEditField_10.Value = 4.0683;

            % Create TausEditField_10Label
            app.TausEditField_10Label = uilabel(app.GridLayout6_9);
            app.TausEditField_10Label.HorizontalAlignment = 'right';
            app.TausEditField_10Label.Layout.Row = 2;
            app.TausEditField_10Label.Layout.Column = 1;
            app.TausEditField_10Label.Text = 'Tau [s]';

            % Create TausEditField_10
            app.TausEditField_10 = uieditfield(app.GridLayout6_9, 'numeric');
            app.TausEditField_10.Layout.Row = 2;
            app.TausEditField_10.Layout.Column = 2;
            app.TausEditField_10.Value = 163.71;

            % Create RetardEditField_5Label
            app.RetardEditField_5Label = uilabel(app.GridLayout6_9);
            app.RetardEditField_5Label.HorizontalAlignment = 'right';
            app.RetardEditField_5Label.Layout.Row = 3;
            app.RetardEditField_5Label.Layout.Column = 1;
            app.RetardEditField_5Label.Text = 'Retard';

            % Create RetardEditField_5
            app.RetardEditField_5 = uieditfield(app.GridLayout6_9, 'numeric');
            app.RetardEditField_5.Layout.Row = 3;
            app.RetardEditField_5.Layout.Column = 2;
            app.RetardEditField_5.Value = 5.2;

            % Create GainslectroniqueTab
            app.GainslectroniqueTab = uitab(app.TabGroup);
            app.GainslectroniqueTab.Title = 'Gains électronique';

            % Create GridLayout2_3
            app.GridLayout2_3 = uigridlayout(app.GainslectroniqueTab);
            app.GridLayout2_3.ColumnWidth = {'1x', '1x', '1.5x', '1x'};
            app.GridLayout2_3.RowHeight = {'1x'};

            % Create GridLayout3_3
            app.GridLayout3_3 = uigridlayout(app.GridLayout2_3);
            app.GridLayout3_3.ColumnWidth = {'fit', '1x'};
            app.GridLayout3_3.RowHeight = {'fit', 'fit', 'fit', 'fit', 'fit'};
            app.GridLayout3_3.Layout.Row = 1;
            app.GridLayout3_3.Layout.Column = 2;

            % Create NbrbitsADCEditFieldLabel
            app.NbrbitsADCEditFieldLabel = uilabel(app.GridLayout3_3);
            app.NbrbitsADCEditFieldLabel.HorizontalAlignment = 'right';
            app.NbrbitsADCEditFieldLabel.Layout.Row = 1;
            app.NbrbitsADCEditFieldLabel.Layout.Column = 1;
            app.NbrbitsADCEditFieldLabel.Text = 'Nbr bits ADC';

            % Create NbrbitsADCEditField
            app.NbrbitsADCEditField = uieditfield(app.GridLayout3_3, 'numeric');
            app.NbrbitsADCEditField.Layout.Row = 1;
            app.NbrbitsADCEditField.Layout.Column = 2;
            app.NbrbitsADCEditField.Value = 10;

            % Create NbrbitsDACEditFieldLabel
            app.NbrbitsDACEditFieldLabel = uilabel(app.GridLayout3_3);
            app.NbrbitsDACEditFieldLabel.HorizontalAlignment = 'right';
            app.NbrbitsDACEditFieldLabel.Layout.Row = 2;
            app.NbrbitsDACEditFieldLabel.Layout.Column = 1;
            app.NbrbitsDACEditFieldLabel.Text = 'Nbr bits DAC';

            % Create NbrbitsDACEditField
            app.NbrbitsDACEditField = uieditfield(app.GridLayout3_3, 'numeric');
            app.NbrbitsDACEditField.Layout.Row = 2;
            app.NbrbitsDACEditField.Layout.Column = 2;
            app.NbrbitsDACEditField.Value = 10;

            % Create OffsetampliT1EditFieldLabel
            app.OffsetampliT1EditFieldLabel = uilabel(app.GridLayout3_3);
            app.OffsetampliT1EditFieldLabel.HorizontalAlignment = 'right';
            app.OffsetampliT1EditFieldLabel.Layout.Row = 3;
            app.OffsetampliT1EditFieldLabel.Layout.Column = 1;
            app.OffsetampliT1EditFieldLabel.Text = 'Offset ampli T1';

            % Create OffsetampliT1EditField
            app.OffsetampliT1EditField = uieditfield(app.GridLayout3_3, 'numeric');
            app.OffsetampliT1EditField.Layout.Row = 3;
            app.OffsetampliT1EditField.Layout.Column = 2;
            app.OffsetampliT1EditField.Value = 1.7;

            % Create OffsetampliT2EditFieldLabel
            app.OffsetampliT2EditFieldLabel = uilabel(app.GridLayout3_3);
            app.OffsetampliT2EditFieldLabel.HorizontalAlignment = 'right';
            app.OffsetampliT2EditFieldLabel.Layout.Row = 4;
            app.OffsetampliT2EditFieldLabel.Layout.Column = 1;
            app.OffsetampliT2EditFieldLabel.Text = 'Offset ampli T2';

            % Create OffsetampliT2EditField
            app.OffsetampliT2EditField = uieditfield(app.GridLayout3_3, 'numeric');
            app.OffsetampliT2EditField.Layout.Row = 4;
            app.OffsetampliT2EditField.Layout.Column = 2;
            app.OffsetampliT2EditField.Value = 1.9;

            % Create OffsetampliT3EditFieldLabel
            app.OffsetampliT3EditFieldLabel = uilabel(app.GridLayout3_3);
            app.OffsetampliT3EditFieldLabel.HorizontalAlignment = 'right';
            app.OffsetampliT3EditFieldLabel.Layout.Row = 5;
            app.OffsetampliT3EditFieldLabel.Layout.Column = 1;
            app.OffsetampliT3EditFieldLabel.Text = 'Offset ampli T3';

            % Create OffsetampliT3EditField
            app.OffsetampliT3EditField = uieditfield(app.GridLayout3_3, 'numeric');
            app.OffsetampliT3EditField.Layout.Row = 5;
            app.OffsetampliT3EditField.Layout.Column = 2;
            app.OffsetampliT3EditField.Value = 2.1;

            % Create LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2 = uilabel(app.GridLayout2_3);
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2.WordWrap = 'on';
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2.Layout.Row = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2.Layout.Column = 1;
            app.LesparamtresdurgulateurConcernentseulementlemodeconsigneLabel_2.Text = 'Les gains et paramètres de l''éléctronique du système. Attention! Ces paramètres ne sont pas modifiables sur le prototype, expérimentez donc avec ces paramètres avec cela en tête.';

            % Create GridLayout3_4
            app.GridLayout3_4 = uigridlayout(app.GridLayout2_3);
            app.GridLayout3_4.ColumnWidth = {'fit', 'fit'};
            app.GridLayout3_4.RowHeight = {'fit', 'fit', 'fit', 'fit', 'fit'};
            app.GridLayout3_4.Layout.Row = 1;
            app.GridLayout3_4.Layout.Column = 3;

            % Create OffsetamplicommandeEditFieldLabel
            app.OffsetamplicommandeEditFieldLabel = uilabel(app.GridLayout3_4);
            app.OffsetamplicommandeEditFieldLabel.HorizontalAlignment = 'right';
            app.OffsetamplicommandeEditFieldLabel.Layout.Row = 1;
            app.OffsetamplicommandeEditFieldLabel.Layout.Column = 1;
            app.OffsetamplicommandeEditFieldLabel.Text = 'Offset ampli commande';

            % Create OffsetamplicommandeEditField
            app.OffsetamplicommandeEditField = uieditfield(app.GridLayout3_4, 'numeric');
            app.OffsetamplicommandeEditField.Layout.Row = 1;
            app.OffsetamplicommandeEditField.Layout.Column = 2;
            app.OffsetamplicommandeEditField.Value = 2.5;

            % Create GainamplicommandeEditFieldLabel
            app.GainamplicommandeEditFieldLabel = uilabel(app.GridLayout3_4);
            app.GainamplicommandeEditFieldLabel.HorizontalAlignment = 'right';
            app.GainamplicommandeEditFieldLabel.Layout.Row = 2;
            app.GainamplicommandeEditFieldLabel.Layout.Column = 1;
            app.GainamplicommandeEditFieldLabel.Text = 'Gain ampli commande';

            % Create GainamplicommandeEditField
            app.GainamplicommandeEditField = uieditfield(app.GridLayout3_4, 'numeric');
            app.GainamplicommandeEditField.Layout.Row = 2;
            app.GainamplicommandeEditField.Layout.Column = 2;
            app.GainamplicommandeEditField.Value = 0.4;

            % Create GainampliT1EditFieldLabel
            app.GainampliT1EditFieldLabel = uilabel(app.GridLayout3_4);
            app.GainampliT1EditFieldLabel.HorizontalAlignment = 'right';
            app.GainampliT1EditFieldLabel.Layout.Row = 3;
            app.GainampliT1EditFieldLabel.Layout.Column = 1;
            app.GainampliT1EditFieldLabel.Text = 'Gain ampli T1';

            % Create GainampliT1EditField
            app.GainampliT1EditField = uieditfield(app.GridLayout3_4, 'numeric');
            app.GainampliT1EditField.Layout.Row = 3;
            app.GainampliT1EditField.Layout.Column = 2;
            app.GainampliT1EditField.Value = 2.94;

            % Create GainampliT2EditFieldLabel
            app.GainampliT2EditFieldLabel = uilabel(app.GridLayout3_4);
            app.GainampliT2EditFieldLabel.HorizontalAlignment = 'right';
            app.GainampliT2EditFieldLabel.Layout.Row = 4;
            app.GainampliT2EditFieldLabel.Layout.Column = 1;
            app.GainampliT2EditFieldLabel.Text = 'Gain ampli T2';

            % Create GainampliT2EditField
            app.GainampliT2EditField = uieditfield(app.GridLayout3_4, 'numeric');
            app.GainampliT2EditField.Layout.Row = 4;
            app.GainampliT2EditField.Layout.Column = 2;
            app.GainampliT2EditField.Value = 4.17;

            % Create GainampliT3EditFieldLabel
            app.GainampliT3EditFieldLabel = uilabel(app.GridLayout3_4);
            app.GainampliT3EditFieldLabel.HorizontalAlignment = 'right';
            app.GainampliT3EditFieldLabel.Layout.Row = 5;
            app.GainampliT3EditFieldLabel.Layout.Column = 1;
            app.GainampliT3EditFieldLabel.Text = 'Gain ampli T3';

            % Create GainampliT3EditField
            app.GainampliT3EditField = uieditfield(app.GridLayout3_4, 'numeric');
            app.GainampliT3EditField.Layout.Row = 5;
            app.GainampliT3EditField.Layout.Column = 2;
            app.GainampliT3EditField.Value = 6.25;

            % Create GridLayout3_5
            app.GridLayout3_5 = uigridlayout(app.GridLayout2_3);
            app.GridLayout3_5.ColumnWidth = {'2x', '1x'};
            app.GridLayout3_5.RowHeight = {'fit', 'fit', 'fit'};
            app.GridLayout3_5.Layout.Row = 1;
            app.GridLayout3_5.Layout.Column = 4;

            % Create TaufiltreT1EditFieldLabel
            app.TaufiltreT1EditFieldLabel = uilabel(app.GridLayout3_5);
            app.TaufiltreT1EditFieldLabel.HorizontalAlignment = 'right';
            app.TaufiltreT1EditFieldLabel.Layout.Row = 1;
            app.TaufiltreT1EditFieldLabel.Layout.Column = 1;
            app.TaufiltreT1EditFieldLabel.Text = 'Tau filtre T1';

            % Create TaufiltreT1EditField
            app.TaufiltreT1EditField = uieditfield(app.GridLayout3_5, 'numeric');
            app.TaufiltreT1EditField.Tooltip = {'Constante de temps du filtre anti-aliasing de T1'};
            app.TaufiltreT1EditField.Layout.Row = 1;
            app.TaufiltreT1EditField.Layout.Column = 2;

            % Create TaufiltreT2EditFieldLabel
            app.TaufiltreT2EditFieldLabel = uilabel(app.GridLayout3_5);
            app.TaufiltreT2EditFieldLabel.HorizontalAlignment = 'right';
            app.TaufiltreT2EditFieldLabel.Layout.Row = 2;
            app.TaufiltreT2EditFieldLabel.Layout.Column = 1;
            app.TaufiltreT2EditFieldLabel.Text = 'Tau filtre T2';

            % Create TaufiltreT2EditField
            app.TaufiltreT2EditField = uieditfield(app.GridLayout3_5, 'numeric');
            app.TaufiltreT2EditField.Tooltip = {'Constante de temps du filtre anti-aliasing de T2'};
            app.TaufiltreT2EditField.Layout.Row = 2;
            app.TaufiltreT2EditField.Layout.Column = 2;

            % Create TaufiltreT3EditFieldLabel
            app.TaufiltreT3EditFieldLabel = uilabel(app.GridLayout3_5);
            app.TaufiltreT3EditFieldLabel.HorizontalAlignment = 'right';
            app.TaufiltreT3EditFieldLabel.Layout.Row = 3;
            app.TaufiltreT3EditFieldLabel.Layout.Column = 1;
            app.TaufiltreT3EditFieldLabel.Text = 'Tau filtre T3';

            % Create TaufiltreT3EditField
            app.TaufiltreT3EditField = uieditfield(app.GridLayout3_5, 'numeric');
            app.TaufiltreT3EditField.Tooltip = {'Constante de temps du filtre anti-aliasing de T3'};
            app.TaufiltreT3EditField.Layout.Row = 3;
            app.TaufiltreT3EditField.Layout.Column = 2;

            % Create ThermistancesTab
            app.ThermistancesTab = uitab(app.TabGroup);
            app.ThermistancesTab.Title = 'Thermistances';

            % Create GridLayout15
            app.GridLayout15 = uigridlayout(app.ThermistancesTab);
            app.GridLayout15.ColumnWidth = {'1x', 'fit', 'fit'};
            app.GridLayout15.RowHeight = {'1x'};

            % Create GridLayout16
            app.GridLayout16 = uigridlayout(app.GridLayout15);
            app.GridLayout16.ColumnWidth = {'fit', 'fit'};
            app.GridLayout16.RowHeight = {'fit', 'fit', 'fit', 'fit'};
            app.GridLayout16.Layout.Row = 1;
            app.GridLayout16.Layout.Column = 2;

            % Create AEditFieldLabel
            app.AEditFieldLabel = uilabel(app.GridLayout16);
            app.AEditFieldLabel.HorizontalAlignment = 'right';
            app.AEditFieldLabel.Layout.Row = 1;
            app.AEditFieldLabel.Layout.Column = 1;
            app.AEditFieldLabel.Text = 'A';

            % Create AEditField
            app.AEditField = uieditfield(app.GridLayout16, 'numeric');
            app.AEditField.Layout.Row = 1;
            app.AEditField.Layout.Column = 2;
            app.AEditField.Value = 0.00335401643468053;

            % Create BEditFieldLabel
            app.BEditFieldLabel = uilabel(app.GridLayout16);
            app.BEditFieldLabel.HorizontalAlignment = 'right';
            app.BEditFieldLabel.Layout.Row = 2;
            app.BEditFieldLabel.Layout.Column = 1;
            app.BEditFieldLabel.Text = 'B';

            % Create BEditField
            app.BEditField = uieditfield(app.GridLayout16, 'numeric');
            app.BEditField.Layout.Row = 2;
            app.BEditField.Layout.Column = 2;
            app.BEditField.Value = 0.000256523550896126;

            % Create CEditFieldLabel
            app.CEditFieldLabel = uilabel(app.GridLayout16);
            app.CEditFieldLabel.HorizontalAlignment = 'right';
            app.CEditFieldLabel.Layout.Row = 3;
            app.CEditFieldLabel.Layout.Column = 1;
            app.CEditFieldLabel.Text = 'C';

            % Create CEditField
            app.CEditField = uieditfield(app.GridLayout16, 'numeric');
            app.CEditField.Layout.Row = 3;
            app.CEditField.Layout.Column = 2;
            app.CEditField.Value = 2.60597012072052e-06;

            % Create DEditFieldLabel
            app.DEditFieldLabel = uilabel(app.GridLayout16);
            app.DEditFieldLabel.HorizontalAlignment = 'right';
            app.DEditFieldLabel.Layout.Row = 4;
            app.DEditFieldLabel.Layout.Column = 1;
            app.DEditFieldLabel.Text = 'D';

            % Create DEditField
            app.DEditField = uieditfield(app.GridLayout16, 'numeric');
            app.DEditField.Layout.Row = 4;
            app.DEditField.Layout.Column = 2;
            app.DEditField.Value = 6.3292612648746e-08;

            % Create GridLayout16_2
            app.GridLayout16_2 = uigridlayout(app.GridLayout15);
            app.GridLayout16_2.ColumnWidth = {'fit', 'fit'};
            app.GridLayout16_2.RowHeight = {'fit', 'fit', 'fit', 'fit'};
            app.GridLayout16_2.Layout.Row = 1;
            app.GridLayout16_2.Layout.Column = 3;

            % Create aEditFieldLabel
            app.aEditFieldLabel = uilabel(app.GridLayout16_2);
            app.aEditFieldLabel.HorizontalAlignment = 'right';
            app.aEditFieldLabel.Layout.Row = 1;
            app.aEditFieldLabel.Layout.Column = 1;
            app.aEditFieldLabel.Text = 'a';

            % Create aEditField
            app.aEditField = uieditfield(app.GridLayout16_2, 'numeric');
            app.aEditField.Layout.Row = 1;
            app.aEditField.Layout.Column = 2;
            app.aEditField.Value = -14.65719769;

            % Create bEditFieldLabel
            app.bEditFieldLabel = uilabel(app.GridLayout16_2);
            app.bEditFieldLabel.HorizontalAlignment = 'right';
            app.bEditFieldLabel.Layout.Row = 2;
            app.bEditFieldLabel.Layout.Column = 1;
            app.bEditFieldLabel.Text = 'b';

            % Create bEditField
            app.bEditField = uieditfield(app.GridLayout16_2, 'numeric');
            app.bEditField.Layout.Row = 2;
            app.bEditField.Layout.Column = 2;
            app.bEditField.Value = 4798.842;

            % Create cEditFieldLabel
            app.cEditFieldLabel = uilabel(app.GridLayout16_2);
            app.cEditFieldLabel.HorizontalAlignment = 'right';
            app.cEditFieldLabel.Layout.Row = 3;
            app.cEditFieldLabel.Layout.Column = 1;
            app.cEditFieldLabel.Text = 'c';

            % Create cEditField
            app.cEditField = uieditfield(app.GridLayout16_2, 'numeric');
            app.cEditField.Layout.Row = 3;
            app.cEditField.Layout.Column = 2;
            app.cEditField.Value = -115334;

            % Create dEditFieldLabel
            app.dEditFieldLabel = uilabel(app.GridLayout16_2);
            app.dEditFieldLabel.HorizontalAlignment = 'right';
            app.dEditFieldLabel.Layout.Row = 4;
            app.dEditFieldLabel.Layout.Column = 1;
            app.dEditFieldLabel.Text = 'd';

            % Create dEditField
            app.dEditField = uieditfield(app.GridLayout16_2, 'numeric');
            app.dEditField.Layout.Row = 4;
            app.dEditField.Layout.Column = 2;
            app.dEditField.Value = -3730535;

            % Create Label_2
            app.Label_2 = uilabel(app.GridLayout15);
            app.Label_2.WordWrap = 'on';
            app.Label_2.Layout.Row = 1;
            app.Label_2.Layout.Column = 1;
            app.Label_2.Interpreter = 'tex';
            app.Label_2.Text = {'Les coéfficients des thermistances. Correspondent aux équations suivantes:'; ''; 't= 1/(A + B \cdot log(r/R_0 ) + C\cdot log(r/R_0 ))^2 + D\cdot log(r/R_0 )^3 ) - 273.15'; ''; 'r = R_0 \cdot exp(A + B/t + C/t^2 + D/t^3 )'};

            % Create TabGroup2
            app.TabGroup2 = uitabgroup(app.GridLayout);
            app.TabGroup2.Layout.Row = 2;
            app.TabGroup2.Layout.Column = 1;

            % Create SignauxTab
            app.SignauxTab = uitab(app.TabGroup2);
            app.SignauxTab.Tooltip = {'Choix des signaux à afficher'};
            app.SignauxTab.Title = 'Signaux';

            % Create GridLayout13
            app.GridLayout13 = uigridlayout(app.SignauxTab);
            app.GridLayout13.ColumnWidth = {'1x'};
            app.GridLayout13.RowHeight = {'1x'};

            % Create Tree
            app.Tree = uitree(app.GridLayout13, 'checkbox');
            app.Tree.Tooltip = {'Cochez les signaux à afficher à l''oscilloscope.'};
            app.Tree.Layout.Row = 1;
            app.Tree.Layout.Column = 1;

            % Create RsistancesNode
            app.RsistancesNode = uitreenode(app.Tree);
            app.RsistancesNode.NodeData = 'None';
            app.RsistancesNode.Text = 'Résistances';

            % Create R_T1Node
            app.R_T1Node = uitreenode(app.RsistancesNode);
            app.R_T1Node.NodeData = 'R_T1';
            app.R_T1Node.Text = 'R_T1';

            % Create R_T2Node
            app.R_T2Node = uitreenode(app.RsistancesNode);
            app.R_T2Node.NodeData = 'R_T2';
            app.R_T2Node.Text = 'R_T2';

            % Create R_T3Node
            app.R_T3Node = uitreenode(app.RsistancesNode);
            app.R_T3Node.NodeData = 'R_T3';
            app.R_T3Node.Text = 'R_T3';

            % Create TensionsNode
            app.TensionsNode = uitreenode(app.Tree);
            app.TensionsNode.NodeData = 'None';
            app.TensionsNode.Text = 'Tensions';

            % Create V_T1Node
            app.V_T1Node = uitreenode(app.TensionsNode);
            app.V_T1Node.NodeData = 'V_T1';
            app.V_T1Node.Text = 'V_T1';

            % Create V_T2Node
            app.V_T2Node = uitreenode(app.TensionsNode);
            app.V_T2Node.NodeData = 'V_T2';
            app.V_T2Node.Text = 'V_T2';

            % Create V_T3Node
            app.V_T3Node = uitreenode(app.TensionsNode);
            app.V_T3Node.NodeData = 'V_T3';
            app.V_T3Node.Text = 'V_T3';

            % Create TempraturesNode
            app.TempraturesNode = uitreenode(app.Tree);
            app.TempraturesNode.NodeData = 'None';
            app.TempraturesNode.Text = 'Températures';

            % Create T1Node
            app.T1Node = uitreenode(app.TempraturesNode);
            app.T1Node.NodeData = 'T1';
            app.T1Node.Text = 'T1';

            % Create T2Node
            app.T2Node = uitreenode(app.TempraturesNode);
            app.T2Node.NodeData = 'T2';
            app.T2Node.Text = 'T2';

            % Create T3Node
            app.T3Node = uitreenode(app.TempraturesNode);
            app.T3Node.NodeData = 'T3';
            app.T3Node.Text = 'T3';

            % Create PRED_T3Node
            app.PRED_T3Node = uitreenode(app.TempraturesNode);
            app.PRED_T3Node.NodeData = 'PRED_T3';
            app.PRED_T3Node.Text = 'PRED_T3';

            % Create AutresNode
            app.AutresNode = uitreenode(app.Tree);
            app.AutresNode.NodeData = 'None';
            app.AutresNode.Text = 'Autres';

            % Create CONSIGNENode
            app.CONSIGNENode = uitreenode(app.AutresNode);
            app.CONSIGNENode.NodeData = 'CONSIGNE';
            app.CONSIGNENode.Text = 'CONSIGNE';

            % Create CMDNode
            app.CMDNode = uitreenode(app.AutresNode);
            app.CMDNode.NodeData = 'CMD';
            app.CMDNode.Text = 'CMD';

            % Create PID_INNode
            app.PID_INNode = uitreenode(app.AutresNode);
            app.PID_INNode.NodeData = 'PID_IN';
            app.PID_INNode.Text = 'PID_IN';

            % Create PID_OUTNode
            app.PID_OUTNode = uitreenode(app.AutresNode);
            app.PID_OUTNode.NodeData = 'PID_OUT';
            app.PID_OUTNode.Text = 'PID_OUT';

            % Create PWM_OUTNode
            app.PWM_OUTNode = uitreenode(app.AutresNode);
            app.PWM_OUTNode.NodeData = 'PWM_OUT';
            app.PWM_OUTNode.Text = 'PWM_OUT';

            % Create AMP_INNode
            app.AMP_INNode = uitreenode(app.AutresNode);
            app.AMP_INNode.NodeData = 'AMP_IN';
            app.AMP_INNode.Text = 'AMP_IN';

            % Create AMP_OUTNode
            app.AMP_OUTNode = uitreenode(app.AutresNode);
            app.AMP_OUTNode.NodeData = 'AMP_OUT';
            app.AMP_OUTNode.Text = 'AMP_OUT';

            % Create PERTURBNode
            app.PERTURBNode = uitreenode(app.AutresNode);
            app.PERTURBNode.NodeData = 'PERTURB';
            app.PERTURBNode.Text = 'PERTURB';

            % Assign Checked Nodes
            app.Tree.CheckedNodes = [app.T1Node, app.T2Node, app.T3Node, app.PRED_T3Node, app.TempraturesNode];

            % Create CommandeTab
            app.CommandeTab = uitab(app.TabGroup2);
            app.CommandeTab.Tooltip = {'Menu de configuration de la simulation en mode commande'};
            app.CommandeTab.Title = 'Commande';

            % Create GridLayout7
            app.GridLayout7 = uigridlayout(app.CommandeTab);
            app.GridLayout7.ColumnWidth = {'1x', 'fit', '1x'};
            app.GridLayout7.RowHeight = {'fit'};

            % Create GridLayout8
            app.GridLayout8 = uigridlayout(app.GridLayout7);
            app.GridLayout8.ColumnWidth = {'fit'};
            app.GridLayout8.RowHeight = {'fit', 'fit'};
            app.GridLayout8.Layout.Row = 1;
            app.GridLayout8.Layout.Column = 3;

            % Create GridLayout9
            app.GridLayout9 = uigridlayout(app.GridLayout8);
            app.GridLayout9.RowHeight = {'1x'};
            app.GridLayout9.Layout.Row = 1;
            app.GridLayout9.Layout.Column = 1;

            % Create DuresEditFieldLabel
            app.DuresEditFieldLabel = uilabel(app.GridLayout9);
            app.DuresEditFieldLabel.HorizontalAlignment = 'right';
            app.DuresEditFieldLabel.Layout.Row = 1;
            app.DuresEditFieldLabel.Layout.Column = 1;
            app.DuresEditFieldLabel.Text = 'Durée [s]';

            % Create DuresEditField
            app.DuresEditField = uieditfield(app.GridLayout9, 'numeric');
            app.DuresEditField.Layout.Row = 1;
            app.DuresEditField.Layout.Column = 2;
            app.DuresEditField.Value = 1000;

            % Create DmarrerButton
            app.DmarrerButton = uibutton(app.GridLayout8, 'push');
            app.DmarrerButton.ButtonPushedFcn = createCallbackFcn(app, @DmarrerButtonPushed, true);
            app.DmarrerButton.Tag = 'start_cmd';
            app.DmarrerButton.Layout.Row = 2;
            app.DmarrerButton.Layout.Column = 1;
            app.DmarrerButton.Text = 'Démarrer';

            % Create PerturbationPanel
            app.PerturbationPanel = uipanel(app.GridLayout7);
            app.PerturbationPanel.Title = 'Perturbation';
            app.PerturbationPanel.Layout.Row = 1;
            app.PerturbationPanel.Layout.Column = 2;

            % Create GridLayout10
            app.GridLayout10 = uigridlayout(app.PerturbationPanel);
            app.GridLayout10.ColumnWidth = {'fit'};
            app.GridLayout10.RowHeight = {'fit', 'fit'};

            % Create Switch
            app.Switch = uiswitch(app.GridLayout10, 'slider');
            app.Switch.Items = {'Non', 'Oui'};
            app.Switch.ItemsData = [0 1];
            app.Switch.Layout.Row = 1;
            app.Switch.Layout.Column = 1;
            app.Switch.Value = 0;

            % Create GridLayout11
            app.GridLayout11 = uigridlayout(app.GridLayout10);
            app.GridLayout11.ColumnWidth = {'fit', '1x'};
            app.GridLayout11.RowHeight = {'fit'};
            app.GridLayout11.Layout.Row = 2;
            app.GridLayout11.Layout.Column = 1;

            % Create TempschelonsEditFieldLabel
            app.TempschelonsEditFieldLabel = uilabel(app.GridLayout11);
            app.TempschelonsEditFieldLabel.HorizontalAlignment = 'right';
            app.TempschelonsEditFieldLabel.Layout.Row = 1;
            app.TempschelonsEditFieldLabel.Layout.Column = 1;
            app.TempschelonsEditFieldLabel.Text = 'Temps échelon [s]';

            % Create TempschelonsEditField
            app.TempschelonsEditField = uieditfield(app.GridLayout11, 'numeric');
            app.TempschelonsEditField.Tooltip = {'Temps auquel la perturbation est déclenchée'};
            app.TempschelonsEditField.Layout.Row = 1;
            app.TempschelonsEditField.Layout.Column = 2;

            % Create CommandePanel
            app.CommandePanel = uipanel(app.GridLayout7);
            app.CommandePanel.Title = 'Commande';
            app.CommandePanel.Layout.Row = 1;
            app.CommandePanel.Layout.Column = 1;

            % Create GridLayout14_2
            app.GridLayout14_2 = uigridlayout(app.CommandePanel);
            app.GridLayout14_2.ColumnWidth = {'1x'};
            app.GridLayout14_2.RowHeight = {'1.33x', '1x'};
            app.GridLayout14_2.RowSpacing = 0;
            app.GridLayout14_2.Padding = [0 0 0 0];

            % Create UITable_2
            app.UITable_2 = uitable(app.GridLayout14_2);
            app.UITable_2.ColumnName = {'Step [s]'; 'Valeur [V]'};
            app.UITable_2.RowName = {};
            app.UITable_2.ColumnSortable = true;
            app.UITable_2.ColumnEditable = true;
            app.UITable_2.Tooltip = {'La valeur de la commande à partir de chaque step. Clic droit pour ajouter des couples.'};
            app.UITable_2.Layout.Row = [1 2];
            app.UITable_2.Layout.Column = 1;

            % Create ConsigneTab
            app.ConsigneTab = uitab(app.TabGroup2);
            app.ConsigneTab.Tooltip = {'Menu de configuration de la simulation en mode consigne'};
            app.ConsigneTab.Title = 'Consigne';
            app.ConsigneTab.Tag = 'start_consigne';

            % Create GridLayout7_2
            app.GridLayout7_2 = uigridlayout(app.ConsigneTab);
            app.GridLayout7_2.ColumnWidth = {'1x', 'fit', '1x'};
            app.GridLayout7_2.RowHeight = {'fit'};

            % Create GridLayout8_2
            app.GridLayout8_2 = uigridlayout(app.GridLayout7_2);
            app.GridLayout8_2.ColumnWidth = {'fit'};
            app.GridLayout8_2.RowHeight = {'fit', '1x', 'fit'};
            app.GridLayout8_2.Layout.Row = 1;
            app.GridLayout8_2.Layout.Column = 3;

            % Create GridLayout9_2
            app.GridLayout9_2 = uigridlayout(app.GridLayout8_2);
            app.GridLayout9_2.RowHeight = {'1x'};
            app.GridLayout9_2.Layout.Row = 1;
            app.GridLayout9_2.Layout.Column = 1;

            % Create DuresEditField_2Label
            app.DuresEditField_2Label = uilabel(app.GridLayout9_2);
            app.DuresEditField_2Label.HorizontalAlignment = 'right';
            app.DuresEditField_2Label.Layout.Row = 1;
            app.DuresEditField_2Label.Layout.Column = 1;
            app.DuresEditField_2Label.Text = 'Durée [s]';

            % Create DuresEditField_2
            app.DuresEditField_2 = uieditfield(app.GridLayout9_2, 'numeric');
            app.DuresEditField_2.Layout.Row = 1;
            app.DuresEditField_2.Layout.Column = 2;
            app.DuresEditField_2.Value = 1000;

            % Create DmarrerButton_2
            app.DmarrerButton_2 = uibutton(app.GridLayout8_2, 'push');
            app.DmarrerButton_2.ButtonPushedFcn = createCallbackFcn(app, @Start_consigne, true);
            app.DmarrerButton_2.Layout.Row = 3;
            app.DmarrerButton_2.Layout.Column = 1;
            app.DmarrerButton_2.Text = 'Démarrer';

            % Create Asserviravecprdictiont3CheckBox
            app.Asserviravecprdictiont3CheckBox = uicheckbox(app.GridLayout8_2);
            app.Asserviravecprdictiont3CheckBox.Text = 'Asservir avec prédiction t3';
            app.Asserviravecprdictiont3CheckBox.Layout.Row = 2;
            app.Asserviravecprdictiont3CheckBox.Layout.Column = 1;
            app.Asserviravecprdictiont3CheckBox.Value = true;

            % Create ConsignePanel
            app.ConsignePanel = uipanel(app.GridLayout7_2);
            app.ConsignePanel.Title = 'Consigne';
            app.ConsignePanel.Layout.Row = 1;
            app.ConsignePanel.Layout.Column = 1;

            % Create GridLayout14
            app.GridLayout14 = uigridlayout(app.ConsignePanel);
            app.GridLayout14.ColumnWidth = {'1x'};
            app.GridLayout14.RowHeight = {'1.33x', '1x'};
            app.GridLayout14.RowSpacing = 0;
            app.GridLayout14.Padding = [0 0 0 0];

            % Create UITable
            app.UITable = uitable(app.GridLayout14);
            app.UITable.ColumnName = {'Step [s]'; 'Valeur [deg C]'};
            app.UITable.RowName = {};
            app.UITable.ColumnSortable = true;
            app.UITable.ColumnEditable = true;
            app.UITable.Layout.Row = [1 2];
            app.UITable.Layout.Column = 1;

            % Create PerturbationPanel_2
            app.PerturbationPanel_2 = uipanel(app.GridLayout7_2);
            app.PerturbationPanel_2.Title = 'Perturbation';
            app.PerturbationPanel_2.Layout.Row = 1;
            app.PerturbationPanel_2.Layout.Column = 2;

            % Create GridLayout10_2
            app.GridLayout10_2 = uigridlayout(app.PerturbationPanel_2);
            app.GridLayout10_2.ColumnWidth = {'fit'};
            app.GridLayout10_2.RowHeight = {'fit', 'fit'};

            % Create Switch_2
            app.Switch_2 = uiswitch(app.GridLayout10_2, 'slider');
            app.Switch_2.Items = {'Non', 'Oui'};
            app.Switch_2.ItemsData = [0 1];
            app.Switch_2.Layout.Row = 1;
            app.Switch_2.Layout.Column = 1;
            app.Switch_2.Value = 0;

            % Create GridLayout11_2
            app.GridLayout11_2 = uigridlayout(app.GridLayout10_2);
            app.GridLayout11_2.ColumnWidth = {'fit', '1x'};
            app.GridLayout11_2.RowHeight = {'fit'};
            app.GridLayout11_2.Layout.Row = 2;
            app.GridLayout11_2.Layout.Column = 1;

            % Create TempschelonsEditField_4Label
            app.TempschelonsEditField_4Label = uilabel(app.GridLayout11_2);
            app.TempschelonsEditField_4Label.HorizontalAlignment = 'right';
            app.TempschelonsEditField_4Label.Layout.Row = 1;
            app.TempschelonsEditField_4Label.Layout.Column = 1;
            app.TempschelonsEditField_4Label.Text = 'Temps échelon [s]';

            % Create TempschelonsEditField_4
            app.TempschelonsEditField_4 = uieditfield(app.GridLayout11_2, 'numeric');
            app.TempschelonsEditField_4.Tooltip = {'Temps auquel la perturbation est déclenchée'};
            app.TempschelonsEditField_4.Layout.Row = 1;
            app.TempschelonsEditField_4.Layout.Column = 2;

            % Create ContextMenu
            app.ContextMenu = uicontextmenu(app.UIFigure);

            % Create AjouterMenu_2
            app.AjouterMenu_2 = uimenu(app.ContextMenu);
            app.AjouterMenu_2.MenuSelectedFcn = createCallbackFcn(app, @Add_row_consigne, true);
            app.AjouterMenu_2.Text = 'Ajouter';
            
            % Assign app.ContextMenu
            app.UITable.ContextMenu = app.ContextMenu;

            % Create ContextMenu2
            app.ContextMenu2 = uicontextmenu(app.UIFigure);

            % Create AjouterMenu
            app.AjouterMenu = uimenu(app.ContextMenu2);
            app.AjouterMenu.MenuSelectedFcn = createCallbackFcn(app, @Add_row_commande, true);
            app.AjouterMenu.Text = 'Ajouter';
            
            % Assign app.ContextMenu2
            app.UITable_2.ContextMenu = app.ContextMenu2;

            % Show the figure after all components are created
            app.UIFigure.Visible = 'on';
        end
    end

    % App creation and deletion
    methods (Access = public)

        % Construct app
        function app = main

            % Create UIFigure and components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            % Execute the startup function
            runStartupFcn(app, @Init)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end